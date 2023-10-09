#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Python 2.x
    from Tkinter import *
    from ttk import *
except ImportError:
    # Python 3.x
    from tkinter import *
    from tkinter.ttk import *

import random

premio = random.randint(1, 3)

def apostar(numero):
    if numero == premio:
        etiqueta.configure(text='¡Ganaste!')
    else:
        etiqueta.configure(text='Lo siento, perdiste.')

ventana = Tk()

ventana.title('Premio')

etiqueta = Label(ventana, text='¿Qué botón es el del premio?')
etiqueta.pack()

for boton in range(1, 4):
    Button(text='Botón ' + str(boton), command=lambda x=boton: apostar(x)).pack(side=LEFT)
    # Si pusiéramos 'command=apostar(boton)' se ejecutaría la función.

ventana.mainloop()