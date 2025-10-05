def safe_divide(numerator, denominator):
    """Performs division and handles division by zero."""
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    return result
