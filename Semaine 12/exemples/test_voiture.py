from unittest import TestCase
from voiture import Voiture


class TestVoiture(TestCase):

    def setUp(self):
        """Initialisation d'une voiture pour les tests."""
        self.voiture = Voiture("Toyota", "Corolla", 2020, 15000)

    def test_kilometrage(self):
        """Test de l'attribut kilometrage."""
        self.assertEqual(self.voiture.kilometrage, 15000)
        with self.assertRaises(ValueError):
            self.voiture.kilometrage = -500

    def test_marque(self):
        """Test de l'attribut marque."""
        self.assertEqual(self.voiture.marque, "Toyota")
        with self.assertRaises(ValueError):
            self.voiture.marque = 10

    def test_modele(self):
        """Test de l'attribut modele."""
        self.assertEqual(self.voiture.modele, "Corolla")
        with self.assertRaises(ValueError):
            self.voiture.modele = 15

    def test_annee(self):
        """Test de l'attribut annee."""
        self.assertEqual(self.voiture.annee, 2020)
        with self.assertRaises(ValueError):
            self.voiture.annee = 1885

        with self.assertRaises(ValueError):
            self.voiture.annee = "2021"

    def test_avancer(self):
        """Test de la méthode avancer."""
        self.voiture.avancer(1, 60)
        self.assertEqual(self.voiture.kilometrage, 15060)

        with self.assertRaises(ValueError):
            self.voiture.avancer(-1, 60)
        with self.assertRaises(ValueError):
            self.voiture.avancer(1, -60)

        self.assertEqual(self.voiture.avancer(2, 100), 200)



