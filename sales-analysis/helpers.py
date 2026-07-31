def calculate_total(quantity,price):
    """claculate total price"""
    return quantity*price

def format_currency(amount):
    """Format number as a currency"""
    return  f'${amount:.,.2f}'