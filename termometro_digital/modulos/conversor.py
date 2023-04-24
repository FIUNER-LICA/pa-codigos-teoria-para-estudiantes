# -*- coding: utf-8 -*-

class Conversor:
    def __init__ (self): 
        self.x_min = 0.0
        self.x_max = 5.0
        self.y_min = -30.0
        self.y_max = 140.0
        
    def convertir (self,p_valor): 
        if isinstance(p_valor,float):
            if self.x_max >= p_valor >= self.x_min:
                m = (self.y_max - self.y_min)/(self.x_max - self.x_min)
                resultado= self.y_min + m*(p_valor - self.x_min)
                return resultado