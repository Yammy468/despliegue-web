"""Pruebas para la función suma del módulo app."""

import unittest
from app import suma

class SumaTest(unittest.TestCase):
    """Clase de pruebas para la función suma."""

    def test_suma_numeros_positivos(self):
        """Prueba la suma de dos números positivos."""
        resultado = suma(1, 2)
        self.assertEqual(resultado, 3)

    def test_suma_cero(self):
        """Prueba la suma de cero con un número positivo."""
        resultado = suma(0, 7)
        self.assertEqual(resultado, 7)

    def test_suma_numeros_invalidos(self):
        """Prueba la suma de dos valores no enteros."""
        resultado = suma("1", "2")
        self.assertIsNone(resultado, "La función no debe aceptar valores no enteros")


