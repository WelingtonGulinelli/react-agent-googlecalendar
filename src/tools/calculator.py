from langchain.tools import tool

@tool
def multiply(a: float, b: float) -> float:
    """
    Multiply a * b and returns the result.

    Args:
        a: float multiplicand
        b: float multiplier

    Returns:
    the resulting float of the equation a * b
    """
    return a * b

@tool
def add(a: float, b: float) -> float:
    """
    Add a + b and returns the result.

    Args:
        a: float addend
        b: float addend 
    Returns:
    the resulting float of the equation a + b
    """
    return a + b

@tool
def subtract(a: float, b: float) -> float:
    """
    Subtract a - b and returns the result.

    Args:
        a: float minuend
        b: float subtrahend
    Returns:
    the resulting float of the equation a - b
    """
    return a - b    

@tool
def divide(a: float, b: float) -> float:
    """
    Divide a / b and returns the result.

    Args:
        a: float dividend
        b: float divisor
    Returns:
    the resulting float of the equation a / b
    """
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a / b    