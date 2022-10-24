# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 10:20:53 2022

@author: dz
"""
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.animation as animation

class InterfazModeloSimulacion:
    
    def __init__(self, p_parametros = 100):
        
        self.cargar_parametros_simulacion(p_parametros)
        
    def cargar_parametros_simulacion(self,p_parametros):
        number = p_parametros
        
        self.data_array = np.zeros(
            number, dtype =[("position", float, (2,)), ("size", float, (1,)), ("color", float, (4,))]
        )
        self.data_array["position"] = np.random.uniform(0, 1, (number, 2))
        self.data_array["size"] = np.linspace(0, 1, number).reshape(number, 1)
        self.data_array["color"][:, 3] = np.linspace(0, 1, number)
        self.epoca = 0
    
    
    def simular_un_paso(self):
        self.data_array["color"][:, 3] = np.maximum(0, self.data_array["color"][:, 3] - 1 / len(self.data_array))
        self.data_array["size"] += 1 / len(self.data_array)

        i = self.epoca % len(self.data_array)
        self.data_array["position"][i] = np.random.uniform(0, 1, 2)
        self.data_array["size"][i] = 0
        self.data_array["color"][i, 3] = 1
        self.epoca += 1

    
    def devolver_datos(self):
        return self.data_array

# def simular_y_graficar(frame,p_scatter,p_im):
#     p_im.simular_un_paso()
#     R = p_im.devolver_datos()
#     p_scatter.set_edgecolors(R["color"])
#     p_scatter.set_sizes(1000 * R["size"].ravel())
#     p_scatter.set_offsets(R["position"])
#     return (p_scatter,)
    
# if __name__ == "__main__":
    
#     fig = plt.figure(figsize=(6, 4), facecolor="white", dpi=100)
#     ax = fig.add_axes([0, 0, 1, 1], frameon=False)  # , aspect=1)
#     scatter = ax.scatter([], [], s=[], linewidth=0.5, edgecolors=[], facecolors="None") 
#     ax.set_xlim(0, 1), ax.set_xticks([])
#     ax.set_ylim(0, 1), ax.set_yticks([])
    
#     im=InterfazModeloSimulacion()

#     animation = animation.FuncAnimation(fig, simular_y_graficar, fargs=(scatter,im,), interval=5)
#     plt.show()