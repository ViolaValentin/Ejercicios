#Definir un procedimientos qie lea los archivos .txt que están en la carpeta marzo, y copie la primera 
#linea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)
#!/usr/bin/env python3
import sys,re,os, glob
def primeras_lineas (carpeta_mes,carpeta_resultado,archivo_salida):
    """
    movemos a marzo
    extraemos los .txt
    leemos las primeras lineas
    hacemos la carpeta de salida
    hacer archivo
    poner lineas en archivo nuevo
    """
    os.chdir (carpeta_mes)
    textos=glob.glob (".txt")
    primera_linea=[]
    for lines in textos:
        with open (lines,"r") as texto:
            primera_linea.append(texto.readline())
    os.chdir ("../../")
    os.mkdir (carpeta_resultado)
    os.chdir (carpeta_resultado)
    with open (archivo_salida,"a") as final_txt:
        primera_lineaStr="".join (primera_linea)
        final_txt.write (primera_lineaStr)

print (primeras_lineas("datos/marzo","resultado","salida.txt"))
"""
#3

def contenido_listas (nombre_archivo,numero_lineas):       
    ultimas_lineas=[]
    todas_las_lineas=[]
    with open (nombre_archivo,"r") as archivo:
            contenido_lineas=(archivo.readlines ()[:numero_lineas])
            todas_las_lineas.append (contenido_lineas)
            lista_invertida=todas_las_lineas.reverse ()
            return (lista_invertida)
print (contenido_listas ("ej1.txt",6))
#no logro inverit la lista
"""