def add_numbers(a: float, b: float) -> float:
    """
    Adds two numbers and returns the result.

    Parameters:
    a (float): The first number to add.
    b (float): The second number to add.

    Returns:
    float: The sum of a and b.

    Raises:
    TypeError: If a or b is not a number.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers.")

    return a + b
