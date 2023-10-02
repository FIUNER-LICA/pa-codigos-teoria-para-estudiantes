# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 08:57:06 2022

@author: dz
"""


import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Animador:
    
    def __init__(self,p_func_ani,p_interval=5):
        self._fig = None
        self._ax = None
        self._scatter = None
        self._animation = None
        self._func_ani = p_func_ani
        self._interval = p_interval
        
        self._fig = plt.figure(figsize=(6, 4), facecolor="white", dpi=100)
        self._ax = self._fig.add_axes([0, 0, 1, 1], frameon=False)  # , aspect=1)
        self._scatter = self._ax.scatter([], [], s=[], linewidth=0.5, edgecolors=[], facecolors="None") 
        self._ax.set_xlim(0, 1)
        self._ax.set_xticks([])
        self._ax.set_ylim(0, 1)
        self._ax.set_yticks([])
        
      
                
    def animar(self):
               
        self._animation = animation.FuncAnimation(self._fig, self._func_ani,fargs=(self._scatter,), interval = self._interval)
        self._plot = plt.show(block = False) 
         
        
    def pausar(self):
        self._animation.pause()
        
        
    def continuar(self):
        self._animation.resume()
    