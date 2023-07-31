# -*- coding: utf-8 -*-


import unittest
from modulos.termometro import Termometro

class TestConversor(unittest.TestCase):
    
    def setUp(self):
        self.termometro = Termometro()
    
    def test_crea_conversor (self): 
       termometro = self.termometro
       self.assertTrue(isinstance(termometro, Termometro))

if __name__ == '__main__':
    unittest.main()