# -*- coding: utf-8 -*-

import unittest
from modulos.conversor import Conversor

class TestConversor(unittest.TestCase):
    
    def setUp(self):
        self.conversor = Conversor()
    
    def test_convertir_en_rango(self):
        conversor = self.conversor
        
        valor_min = conversor.convertir(0.0)
        
        self.assertAlmostEqual(-30.0, valor_min)
    
    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()