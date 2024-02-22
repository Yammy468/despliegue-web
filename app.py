""" Docstring del módulo """

def suma(a: int, b: int) -> int:
    """
    Esta función realiza una operación específica.

    Args:
        a (int): Primer parámetro.
        b (int): Segundo parámetro.

    Returns:
        int: El resultado de la operación.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Ambos argumentos deben ser números enteros")

    return a + b