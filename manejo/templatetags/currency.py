from decimal import Decimal, InvalidOperation
from django import template

register = template.Library()


@register.filter(name='currency_qtz')
def currency_qtz(value):
    """Format number as Quetzales with comma thousands and 2 decimals, prefixed with 'Q '.

    Examples:
        5000 -> 'Q 5,000.00'
        -5000 -> 'Q -5,000.00'
    """
    try:
        val = Decimal(value)
    except (InvalidOperation, TypeError, ValueError):
        try:
            val = Decimal(str(value))
        except Exception:
            return value
    # format works with Decimal: includes thousands separator and two decimals
    formatted = format(val, ",.2f")
    return f"Q {formatted}"
