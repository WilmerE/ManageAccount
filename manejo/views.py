from django.shortcuts import render
from django.db.models import Sum
from django.core.paginator import Paginator
from decimal import Decimal
from .models import Ingreso, Salida, Entrada


def home(request):
    # Obtener la entrada más reciente para el título y descripción del proyecto
    entrada = Entrada.objects.order_by('-creado').first()
    
    # Suma total de ingresos (saldo inicial)
    inicial = Ingreso.objects.aggregate(total=Sum('monto'))['total'] or Decimal('0')

    # Listado de salidas (ordenadas por fecha desc)
    salidas_qs = Salida.objects.order_by('-creado')
    suma_raw = salidas_qs.aggregate(total=Sum('monto'))['total'] or Decimal('0')

    # Normalizar suma de salidas: tratar como valor positivo de outflow
    try:
        suma_raw = Decimal(suma_raw)
    except Exception:
        suma_raw = Decimal(str(suma_raw))

    suma_salidas = -suma_raw if suma_raw < 0 else suma_raw

    # Paginación: 10 por página
    page_number = request.GET.get('page', 1)
    paginator = Paginator(salidas_qs, 10)
    page_obj = paginator.get_page(page_number)

    # Saldo actual: saldo inicial - suma de salidas
    try:
        inicial = Decimal(inicial)
    except Exception:
        inicial = Decimal(str(inicial))

    actual = inicial - suma_salidas

    context = {
        'entrada': entrada,
        'saldo_inicial': inicial,
        'salidas_page': page_obj,
        'suma_salidas': suma_salidas,
        'saldo_actual': actual,
    }
    return render(request, 'manejo/home.html', context)
from django.shortcuts import render

# Create your views here.
