from generador import *
from soporte import *
import os

opcion = 0
archivo = open('series.dat', 'rb')
pickle.load(archivo)

while opcion != 7:
    print('¿Bienvenido a UTNFlix, qué desea hacer hoy?')
    print('1) Mostrar las series de series.dat ordenadas por título.')
    print('2) Generar una lista de n series de un género específico.')
    print('3) Determinar la cantidad de series por género y por idioma.')
    print('4) Buscar una serie con un título específico.')
    print('5) Mostrar series que el usuario aún no ha empezado a ver.')
    print('6) Generar un archivo con series que tengan más de una temporada de un idioma específico.')
    print('7) Salir.')
    print()
    opcion = int(input('Seleccione una opción: '))

    if opcion == 1:
        mostrar('series.dat', archivo)
        resp = input('¿Desea realizar otra operación? (S/N) ')
        if resp == 'S' or resp == 's':
            opcion = 0
        if resp == 'N' or resp == 'n':
            print('¡Gracias por contar con nuestros servicios!')
            opcion = 7

if opcion == 2:
    listan()

if opcion == 3:
    generidio()

if opcion == 4:
    portitulo()

if opcion == 5:
    nolasvio()

if opcion == 6:
    enidio()

if opcion == 7:
    archivo.close()
