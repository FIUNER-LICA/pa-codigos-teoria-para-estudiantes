# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:20:34 2022

@author: dz
"""
from modelo import InterfazModeloSimulacion
from animador import Animador


class ControladorDeSimulador:
    
    def __init__(self):
        self.im = InterfazModeloSimulacion()
        self.animador = Animador(p_func_ani = self._syg)
        
    def fijar_parametros_simulacion(self,p_parametros_simulacion):
        self.im.cargar_parametros_simulacion(p_parametros_simulacion)
  
    def _syg(self,frame,p_scatter):
        self.im.simular_un_paso()
        R = self.im.devolver_datos()
        p_scatter.set_edgecolors(R["color"])
        p_scatter.set_sizes(1000 * R["size"].ravel())
        p_scatter.set_offsets(R["position"])
        return (p_scatter,)
    
    def simular_y_graficar(self):
        self.im.cargar_parametros_simulacion(100)
        self.animador.animar()
    
    def pausar_simulacion(self):
        self.animador.pausar()
    
    def continuar_simulacion(self):
        self.animador.continuar()
    
        
if __name__ == "__main__":
    cs = ControladorDeSimulador()
    cs.simular_y_graficar()
    
