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

def reemplazar2 (string):
    return (re.sub("(\W)",'_',string,count=2))

print (reemplazar2 (("Hoy523@es@@tuvimos trabajand735o con re -regul74ar expr52ession- en py@th532523on -con VSC532ode-")))


#14
""""Realizá un programa que reemplace los espacios y tabulaciones por punto y coma."""

def reemplazar (string):
    return string.replace(" ",";").replace("    ",";")
    
print (reemplazar (("hola_a todas y: todos ")))

#15
""""Realizá un programa que validar si una cuenta de mail está escrita correctamente."""

def verificar_string (string):
    return (re.search(r"[a-z0-]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*",string))

#^[a-z0-9]+[.-_]?[a-z0-9]+@[a-z]+[.][a-z]+[.]?[a-z]?$
print (verificar_string (("valentinviola@gmail.com")))

""""def verificar_string (string):
    return (re.search("Hola\sbuen\sdia",string))

print (verificar_string("Hola buen dia"))"""
#Manipulación de archivos

