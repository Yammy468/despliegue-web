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
        return None

    return a + b

# Nueva línea agregada
