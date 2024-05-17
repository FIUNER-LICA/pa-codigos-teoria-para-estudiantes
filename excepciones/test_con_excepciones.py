import unittest
from excepciones.clases import Cajon, Alimento, Kiwi


class TestCajon(unittest.TestCase):
    def setUp(self) -> None:
        self.cajon = Cajon()
        return super().setUp()
    
    def test_agregar_alimento_a_cajon(self):
        self.cajon.agregar_alimento(Kiwi())
        # self.cajon.agregar_alimento(Fruta())  # No tiene sentido
        for alimento in self.cajon:
            self.assertTrue(isinstance(alimento, Alimento))
        
    def test_agregar_alimento_a_cajon_lanza_excepcion(self):
        with self.assertRaises(TypeError):
            self.cajon.agregar_alimento('papa')
            

if __name__ == '__main__':
    unittest.main()

    # alimento = Alimento()     # Falla
    # fruta = Fruta()           # Falla
    # kiwi = Kiwi()             # Anda