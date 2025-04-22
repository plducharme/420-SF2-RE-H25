# test_simple_math.py
import unittest
from simple_math import SimpleMath


class SimpleMathTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = SimpleMath(2)

    def test_somme(self):
        self.assertEqual(SimpleMath.somme(1, 1), 2)

    def test_soustraction(self):
        self.assertEqual(self.instance.soustraction(2, 1), 1)

    def test_somme_liste(self):
        self.assertEqual(self.instance.somme_liste([1, 2, 3, 4]), 10)

    def test_conversion_base_10(self):
        self.assertEqual(self.instance.conversion_base_10(10), 2)
        self.assertEqual(self.instance.conversion_base_10(11), 3)
        self.assertEqual(self.instance.conversion_base_10(100), 4)
        self.assertEqual(self.instance.conversion_base_10(1001), 9)

        # Tester la conversion d'un nombre dans une base invalide
        # La base doit être entre 2 et 10
        # Le test doit lever une exception ValueError
        with self.assertRaises(ValueError):
            self.instance.conversion_base_10(20)

        with self.assertRaises(ValueError):
            self.instance.conversion_base_10(-1)

        # Tester avec une autre base
        self.instance.base = 6
        self.assertEqual(self.instance.conversion_base_10(10), 6)
        self.assertEqual(self.instance.conversion_base_10(11), 7)

    def test_division(self):
        self.assertEqual(SimpleMath.division(10, 2), 5)
        # Tester la division par zéro, le test doit lever une exception
        with self.assertRaises(ValueError):
            SimpleMath.division(10, 0)

        # Compare le nombre jusqu'à la troisième décimale
        self.assertAlmostEqual(SimpleMath.division(10, 3), 3.333, places=3)


if __name__ == '__main__':
    unittest.main()
