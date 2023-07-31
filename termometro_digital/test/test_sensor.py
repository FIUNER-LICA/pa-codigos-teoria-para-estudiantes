# -*- coding: utf-8 -*-
import unittest
from modulos.sensor import Sensor

class TestSensor(unittest.TestCase):
    
    def setUp(self):
        pass  
    
    def test_sensar_valor_en_rango(self):
        sensor = Sensor()
        valor_en_rango = True
        
        for i in range(500):
            valor = sensor.sensar()
            if valor < 0.0 and valor > 5.0:
                valor_en_rango = False
                
        self.assertTrue(valor_en_rango)

if __name__ == '__main__':
    unittest.main()