#el vector se llama agenda y la matriz se llama mat
def item3(agenda):
    #Crear el vector
    for i in range(len(agenda)):
        f = agenda[i].tipoContacto
        c = agenda[i]. genero
        mat[f][c]+= 1
    return mat

#Mismo ejercicio pero para un archivo
import os
def item3_b(FD):
    if not os.path.exists(FD):
        print("Archivo inexistente")
        return
    #Crear matriz con ceros
    m = open(FD,'rb')
    t = os.path.getsize(FD)
    while m.tell()< t:
        reg = reg.tipoContacto
        c = reg.genero
        mat[f][c]+=1
    m.close()
    return mat