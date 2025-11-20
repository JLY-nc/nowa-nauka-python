def calcualte_total(quantity, price):
    """Zsumuj wartość dla jednego przedmiotu"""
    return quantity * price


def format_currency(amount):
    """Sformatowanie liczby jako waluty"""
    return f"${amount:,.2f}"
