def trasladar(una_lista, otra_lista, elemento):
  otra_lista.append(elemento)
  una_lista.remove(elemento)

lista = [2,5,8]
listita = []
trasladar(listita, lista, 2)

"""El tipo de error es ValueError, lo que nos indica que el elemento que se queire remover no 
se encuentra en la lista. Par caprtura esa excepción debemos hacer lo siguiente:"""

def trasladar(una_lista, otra_lista, elemento):
    try:
        otra_lista.append(elemento)
        una_lista.remove(elemento)
    except ValueError:
       return ("El valor que se quiere eliminar no existe")
lista = [2,5,8]
listita = [2,3,4]
trasladar(listita, lista, 2)
