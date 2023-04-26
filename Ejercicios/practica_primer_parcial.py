#Expresiones regulares
import re,sys,glob,os   
#1
"""Escribí un programa que verifique si un string 
tiene al menos un carácter permitido. Estos caracteres son a-z, A-Z y 0-9."""
""""
def verificar_string (string):
    return bool (re.search("[a-zA-Z0-9]",string))

print (verificar_string (("En este string hay 20 caracteres")))
"""

#2
"""Escribí un programa que verifique si un string 
tiene todos sus caracteres permitidos. Estos caracteres son a-z, A-Z y 0-9."""

""""def verificar_string(string):

        return bool (re.search("r[^a-zA-Z0-9]+",string))

print (verificar_string (("Enestestri@nghaycaracteres")))"""

#3
""""
Creá un programa que verifique las siguientes condiciones:
si un string dado tiene una h seguida de ninguna o más e.
si un string dado tiene una h seguida de una o más e.
si un string dado tiene una h seguida de cero o una e.
si un string dado tiene una h seguida de dos o tres e."""

"""def verificar_string (string,patron):
    return bool (re.search(patron,string))

print (verificar_string ("En este string hay 20 caracteres","he*"))
print (verificar_string ("En este string heay 20 caracteres","he+"))
print (verificar_string ("En este string hay 20 caracteres","he?"))
print (verificar_string ("En este string hay 20 hecarheacteres","[he]{2,3}"))
"""

#4
""""Realizá un programa que encuentre una palabra unida a otra con un 
guión bajo en un string dado (el string no debe contener espacios)."""

""""def verificar_string (string,palabra1,palabra2):
    patron=f"{palabra1}_{palabra2}"
    return (re.search(patron,string))

print (verificar_string ("Enestestring_hay20_caracteres","string","hay"))"""

#5
"""
Escribí un programa que diga si un string empieza con un número específico.
"""

""""def verificar_string (string,numero):
    return bool (re.search(f"^{numero}",string))

print (verificar_string ("2En este string hay 20 caracteres",4))"""

#6

""""Escribí un programa que dada una lista de strings verifique si se encuentran en una frase dada."""


""""def verificar_string (string):

    for secuencia in string:
        if secuencia in string:
            print ("Está")
        else:
            print ("No está")

lista=["hay","caracteres","eavews"]
print (verificar_string ("En este string hay 20 caracteres"))"""

#7
"""Realizá un programa que encuentre un string que contenga solamente 
letras minúsculas, mayúsculas, espacios y números."""

""""def verificar_string (string):
    return bool (re.search("[a-zA-z0-9]+\s+",string))

print (verificar_string (("Enestest ringhay20caracteres")))
"""
#8
""""Escribí un programa que separe y devuelva los caracteres númericos de un string."""
""""def verificar_string (string):
    return (re.findall("\d+",string))

print (verificar_string (("Enes10test ringhay20carac30teres")))
"""
#9
"""Escribí un programa que extraiga los caracteres que estén entre guiones en un string. 
(String de ejemplo: "Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")"""

"""'def verificar_string (string):
    return (re.findall("-(.*?)-",string))

print (verificar_string (("Hoy estuvimos trabajando con re -regular expression- en python -con VSCode-")))
"""
#10
""""Obtené las substrings y las posiciones de estas en una string dada considerando 
que las substrings están delimitadas por los caracteres @ o &.s"""
""""def sub_strings (string):
    return (re.findall("@(.*?)&.s",string))
    
print (sub_strings (("fewvewwev @ewvew&.s  fevae&.s fqc&.s afe@vew&.s")))
"""
#11
"""
Realizá un programa que dado una lista de strings verifique que dos palabras dentro del 
string empiecen con la letra P y las imprima.
 (Lista de ejemplo: ["Práctica Python", "Práctica C++", "Práctica Fortran"]).
"""
""""def string_letra_p (lista):
    for i in lista:
        patron="(P\w*) (P[a-z]*)"
        print (re.findall(patron,i))

print (string_letra_p (["Prática Python", "Práctica C++", "Práctica Fortran"]))"""
#CONSULTAR POR LOS ESPACIOS

#12
""""Escribí un programa que reemplace todas las ocurrencias de 
espacios, guiones bajos y dos puntos por la barra vertical (|)."""
""""def sub_strings (string):
    return string.replace("_","|").replace(" ","|").replace(":","|")
    
print (sub_strings (("hola_a todas y: todos")))"""

#13
""""Escribí un programa que reemplace los dos primeros caracteres no alfanúmericos por guiones bajos."""

"""def reemplazar2 (string):
    return (re.sub("(\W)",'_',string,count=2))

print (reemplazar2 (("Hoy523@es@@tuvimos trabajand735o con re -regul74ar expr52ession- en py@th532523on -con VSC532ode-")))

"""
#14
""""Realizá un programa que reemplace los espacios y tabulaciones por punto y coma."""

"""def reemplazar (string):
    return string.replace(" ",";").replace("    ",";")
    
print (reemplazar (("hola_a todas y: todos ")))"""

#15
""""Realizá un programa que validar si una cuenta de mail está escrita correctamente."""
"""
def verificar_string (string):
    return (re.search(r"[a-z0-]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*",string))

#^[a-z0-9]+[.-_]?[a-z0-9]+@[a-z]+[.][a-z]+[.]?[a-z]?$
print (verificar_string (("valentinviola@gmail.com")))"""

""""def verificar_string (string):
    return (re.search("Hola\sbuen\sdia",string))

print (verificar_string("Hola buen dia"))"""
#Manipulación de archivos

#1
"""Realizá un programa que lea un archivo e imprima cuántas líneas de ese archivo no empiezan con 
una determinada letra (por ejemplo que imprima cuántas líneas no empiezan con "P")."""

""""def lineas_con_p (archivo,letra):
    contador=0
    with open (archivo, "r") as arch:
       for linea in arch:
           if (linea[0] != letra.lower() and linea[0] !=letra.upper()):
               contador+=1
    return contador  

print (lineas_con_p ("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","P"))
"""
#otra forma mas corta pero solo toma o p o P

""""def lineas_con_p2 (archivo,letra):
    contador=0
    with open(archivo, "r") as archivo:
        for linea in archivo:
            if linea.startswith(letra):
                contador += 1
        return contador
print (lineas_con_p2 ("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","p"))      
"""
#2
""""Escribí un programa que lea un archivo e imprima las primeras n líneas."""
""""
def primeras_lineas (archivo,numero_de_lineas):
    with open (archivo,"r") as archivo:
        lineas_de_archivo=archivo.readlines ()[:numero_de_lineas]
        return lineas_de_archivo
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt",4))
"""
#3
""""Escribí un programa que lea un archivo, guarde las líneas
 del archivo en una lista y luego imprima las n últimas."""

""""def primeras_lineas (archivo,numero_de_lineas):
    with open (archivo,"r") as archivo:
        lineas_de_archivo=archivo.readlines ()[-numero_de_lineas:]

        return lineas_de_archivo
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt",1))
"""
#4
""""Hacé un programa que lea un archivo, cuente la cantidad de
 palabras del archivo y luego imprima el resultado."""
""""def primeras_lineas (archivo):
    with open (archivo,"r") as archivo:
        lineas_de_archivo=archivo.read ()
        lineas_de_archivoStr="".join(lineas_de_archivo)
        return (len (re.split (" |\n",lineas_de_archivoStr)))
       
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt"))
"""
#5
""""Escribí un programa que lea un archivo, reemplace una letra por 
esa misma letra más un salto de línea y lo guarde en otro archivo."""
""""
def primeras_lineas (archivo,letra):
    with open (archivo,"r") as archivo:
        archivo_leido=archivo.read ()
        return archivo_leido.replace (letra,f"{letra}\n")
       
       
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","P"))
"""
#6
''''Realizá un programa que lea un archivo, elimine todos los saltos de línea y lo guarde en otro archivo.'''

""""def primeras_lineas (archivo,archivo2):
    with open (archivo,"r") as archivo:
        archivo_leido=archivo.read ()
        archivo_reemplazado= archivo_leido.replace ("\n","")
        with open (archivo2,"a") as archivo2:
            archivo2.write (archivo_reemplazado)
       
print (primeras_lineas("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","archiv2"))"""

#7
"""Escribí un porgrama que lea un archivo e identifique la palabra más larga, 
la cual debe imprimir y decir cuantos caracteres tiene."""

""""def palabra_mas_larga (archivo):
    with open (archivo,"r") as archivo:
longitud_maxima = 0
    for palabra in archivo_leido:
        if len(palabra) > longitud_maxima:
            longitud_maxima = len(palabra)
            palabra_mas_larga = palabra
            return (palabra_mas_larga)

print (palabra_mas_larga("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt"))"""

#8
"""
Escribí un programa que abra dos documentos y guarde el contenido de ambos en un otro documento ya existente.
"""

""""def contenido_archivos (archivo1,archivo2,archivo3):
    with open (archivo1,"r") as arch1, open (archivo2,"r") as arch2, open (archivo3,"a") as arch3:
        archivos_leidos=arch1.read()
        archivos_leido2=arch2.read()
        archivos_leidos3=archivos_leidos+archivos_leido2
        return arch3.write(archivos_leidos3)
print (contenido_archivos("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo_arch.txt","archivo_completo.txt"))
"""
#9
"""
Realizá un programa que lea un archivo y obtenga la frecuencia de 
cada palabra que hay en el archivo. Recordá que la frecuencia es la 
relación entre número de veces que aparece 
la palabra en cuestión con respecto a la cantidad total de palabras.
"""
def frecuencia (archivo,palabra):
    contador=0
    with open (archivo,"r") as arch1:
        arch1_leido=arch1.read()
        arch1_leido_lista=re.split (" |\n",arch1_leido)
        len_arch1_leido_lista=len(arch1_leido_lista)
        for palabra_buscada in arch1_leido_lista:
            if palabra in palabra_buscada:
                contador+=1
    return ("La frecuencia de la palabra es", (contador*100)/len_arch1_leido_lista), contador
print (frecuencia("C:\\Users\\valen\\Ejercicios\\Ejercicios\\nuevo.txt","ponelo"))

#10
"""
Escribí un programa que lea todos los archivos .txt de una carpeta dada (Carpeta1) 
y los añada a un archivo dentro de la carpeta Resultado, 
que a su vez se tiene que encontrar dentro de Carpeta1.
"""