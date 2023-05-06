#Definir un procedimientos que lea los archivos .txt que están en la carpeta marzo, y copie la primera 
#linea de cada uno en un archivo dentro de la carpeta resultados (que debe estar dentro de new)
#!/usr/bin/env python3
import re,glob,sys,os

def archivos_marzo(path_carpeta,archivo_salida):
    #muevo a carpeta marzo
    #traigo archivos txt
    #leo primera linea de codigo
    #creo la carpeta resultados
    #me muevo a ala carpeta
    #escribo esas lineas en un archivo

    os.chdir (path_carpeta) #me muevo a la carpeta marzo
    txt=glob.glob("*.txt")
    primeras_lineas=[]
    for archivos_txt in txt:
        with open (archivos_txt,"r") as arch_txt:
            primeras_lineas.append(arch_txt.readline())

            os.chdir ("../../")
            os.mkdir ("./resultados")
            os.chdir ("./resultados")
            with open (archivo_salida,"a") as arch_salida:
                primeras_lineasStr="".join(primeras_lineas)
                arch_salida.write(primeras_lineasStr)
