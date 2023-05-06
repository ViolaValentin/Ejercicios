"""
Realizá un programa que lea un archivo y obtenga la frecuencia de 
cada palabra que hay en el archivo. Recordá que la frecuencia es la 
relación entre número de veces que aparece 
la palabra en cuestión con respecto a la cantidad total de palabras.
"""
def frecuencia(archivo):
    with open(archivo, "r") as arch:
        archivo_leido = arch.read().split()
        cantidad_de_palabras = len(archivo_leido)
        lista_palabras_unicas = set(archivo_leido)

        for palabra in lista_palabras_unicas:
            cantidad_de_veces = archivo_leido.count(palabra)
            frecuencia = (cantidad_de_veces / cantidad_de_palabras) * 100
            print(f"La palabra '{palabra}' aparece {frecuencia} veces")

frecuencia("C:\\Users\\valen\\Ejercicios\\Repasando_parcial\\man_arch\\archivo_frecuencia.txt")

        