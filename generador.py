import pickle
import random
import soporte
import os


class Serie:
    def __init__(self, cod, nom, gen, idio, temps, caps, dur, utem, ucap):
        Serie.ID = cod
        Serie.nombre = nom
        Serie.genero = gen
        Serie.idioma = idio
        Serie.temporadas = temps
        Serie.capitulos = caps
        Serie.duracion = dur
        Serie.lastemp = utem
        Serie.lastcap = ucap


def generar(iter):
    m = open('series.dat', 'wb')
    for i in range(iter):
        cod = i
        nom = 'Serie ' + chr(random.randint(97, 122)) + chr(random.randint(97, 122)) + chr(random.randint(97, 122))
        gen = str(random.randint(0, 5))
        idiom = str(random.randint(0, 4))
        ctemps = str(random.randint(0, 12))
        ccaps = str(random.randint(0, 12))
        duran = str(random.randint(30, 59))
        utemp = str(random.randint(0, int(ctemps)))
        ucap = str(random.randint(0, int(ccaps)))
        serie = Serie(cod, nom, gen, idiom, ctemps, ccaps, duran, utemp, ucap)
        pickle.dump(serie, m)
    m.close()

if __name__ == '__main__':
    veces = int(input('¿Cuántas series desea crear? '))
    generar(veces)
# Título o nombre
# Género: 0-Infantil, 1-Comedia, 2-Romántico, 3-Drama, 4-Ciencia Ficción, 5-Otros.
# Idioma Original: 0-Español, 1: Inglés, 2: Francés, 3: Portugués, 4:Otros.
# Cantidad de temporadas.
# Cantidad de capítulos por temporada (suponiendo que todas tienen la misma cantidad)
# Duración de cada capítulo en minutos (suponiendo la misma para todos los de la serie)
# Última temporada vista (si aún no vio la serie vale 0)
# Último capítulo visto
