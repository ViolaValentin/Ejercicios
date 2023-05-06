import sys,re,glob,os
"""Escribí un programa que lea todos los archivos .txt de una carpeta dada 
(Carpeta1) y los añada a un archivo dentro de la carpeta Resultado, 
que a su vez se tiene que encontrar dentro de Carpeta1."""

def leyendo_txt (Carpeta1, archivo_salida):
    #me muevo a carpeta1
    #agarro todos los txt
    #los leo
    #me muevo a carpeta1
    #creo archivo resultado en Carpeta1
    #escribo el archivo

    os.chdir (Carpeta1)
    txt=glob.glob("*.txt")
    archivos_leidos=[]
    for leer_archivos in txt:
        with open (leer_archivos, "r") as leer_arch:
            archivos_leidos.append(leer_arch.read())
    os.mkdir ("./Resultados")
    os.chdir("./Resultados")
    with open (archivo_salida,"a") as arch_salida:
        archivos_leidosStr="".join(archivos_leidos)
        arch_salida.write (archivos_leidosStr)
leyendo_txt ("./Carpeta1","salida.txt")

