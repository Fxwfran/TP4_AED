import pickle
import os
import generador


def mostrar(nombre, archivo):
    v = []
    tamaño = os.path.getsize(nombre)
    while archivo.tell() < tamaño:
        swag = pickle.load(archivo)
        v.append(swag)
    print(v)


def listan():
    pass


def generidio():
    pass


def portitulo():
    pass


def nolasvio():
    pass


def enidio():
    pass
