# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:17:52 2022

@author: jorda
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Graficador:
    '''
    
    '''
    
    def __init__(self):
        self.X = None
        self.C = None
        self.S = None
        self.line1 = None
        self.line2 = None
        self.animador = None
        self.cuadro = 0
        
    def animar_y_graficar(self):
        fig = plt.figure(figsize=(7,2), dpi=100)
        ax = plt.subplot()

        self.X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
        self.C, self.S = np.cos(self.X), np.sin(self.X)

        self.line1, = ax.plot(self.X, self.C, marker="o", markevery=[-1],
        markeredgecolor="white")
        self.line2, = ax.plot(self.X, self.S, marker="o", markevery=[-1],
        markeredgecolor="white")

        self.animador = animation.FuncAnimation(fig, self._update, 
                                                interval=10, 
                                                fargs=(1,2,3),
                                                frames=50)
        plt.show()
        
    def _update(self, frame, *fargs):
        self.cuadro = frame
        self.line1.set_data(self.X[:frame], self.C[:frame])
        self.line2.set_data(self.X[:frame], self.S[:frame])
        print('fargs:', fargs, '  -  cuadro:', self.cuadro)

        
        
if __name__ == '__main__':
    g = Graficador()
    
    g.animar_y_graficar()
        