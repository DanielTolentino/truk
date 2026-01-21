from django import template

register = template.Library()

@register.filter
def compact_number(value):
    """Formata números grandes de forma compacta (ex: 24K, 24.5K)"""
    try:
        value = float(value)
        if value >= 1000:
            k_value = value / 1000
            if k_value >= 10:
                return f"{k_value:.0f}K"
            else:
                return f"{k_value:.1f}K"
        return f"{value:.0f}"
    except (ValueError, TypeError):
        return value
