# hack para importar desde directorio hermano
from sys import path
from os.path import dirname as dir
path.append(dir(path[0]))


# código de la prueba
import unittest
from poo.termometro import Termometro, Conversor


class TestTermometro(unittest.TestCase):

    def setUp(self) -> None:
        self.termometro = Termometro()
        # print("setUp")

    def test_la_temperatura_esta_en_rango(self):
        # termometro = Termometro()
        for _ in range(1000):
            temperatura = self.termometro.medirTemperatura()
            self.assertGreaterEqual(temperatura, -20)
            self.assertLessEqual(temperatura, 120)

    def test_el_termometro_tiene_un_conversor(self):
        self.assertIsInstance(self.termometro._Termometro__conversor, Conversor)

    # def tearDown(self) -> None:
        # print("tearDown")
    

if __name__ == "__main__":
    unittest.main()
