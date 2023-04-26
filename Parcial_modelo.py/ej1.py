import re
def secuencias_ab (string):
    return re.findall ("[^X][ab]+[^Y]",string)
#(.*)?(.*)?
print (secuencias_ab("XbaaaYjXababYqxbabbbbaaffeeY"))
""""
import re
def funcion_de_expresiones_regulares(string):
    return re.findal ("ag(\d.*?)cta",string)

print (funcion_de_expresiones_regulares("aabocaggaaactazu4lggaasag24gra1ndecta"))
"""
#b)

""""
a) El nombre de la función... No respeta las convenciones de nombre de Pyhton ya que no separa las palabras con (_)
b) La función lanza NameError... La función lanza AtributeError, que indica que no existe un atributo llamado findal, el atributo correcto es findall
c) La función lanza Sintax... Sintaz error refiere a errores en la construcción del código, por ejemplo, print (Hola mundo")
d) Una vez corregida...["gaaa"]...No devuelve esta búsqueda porque e ningún momento coincide el patrón.
e) Una vez corregida... ["24gra"]...[x] Este patrón, si puede encontrarse en el string enviado.

"""