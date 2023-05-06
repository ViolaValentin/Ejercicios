import re
'''
Buscar en un string todos los numeros de telefono de capital federal
'''

def numeros_capital(string):
    return re.findall ("([+]54-911[0-9]{8})",string)

print (numeros_capital("52623+322+564+26243+623+32+43vreberbe5+berberberb+54-9115323535364364362+236362+g43g+54-911634892988923682393vre"))

"""Encontrar direcciones en una cadena de texto:
def direcciones (string):
    return re.findall ("([a-zA-z])([0-9]{4})",string)

print (direcciones("Senillosa532532532532532vwrnvewbiewuobnewinewngiuenwvSenillosa433ewvmewiewiomvwv,ew.we.gew.ge.w.egwg.we.gew.gegw.vewveSenillosa56132532"))

"""
"""Encontrar todas las fechas en formato "dd/mm/aaaa" en una cadena de texto:"""
def fechas (string):
    return re.findall ("\d{2}[/]\d{2}[/]\d{4}",string)

print (fechas ("Hoy es 01/05/2023 y mañana será 02/05/2023432."))

"""Encontrar todas las palabras que comiencen con una letra mayúscula en una cadena de texto:"""

def palabras_mayusculas (string):
    return re.findall ("([A-Z][a-z]+)",string)
print (palabras_mayusculas("El Perro Saltó Por Encima De La Valla."))

""""Encontrar todas las direcciones de correo electrónico en una cadena de texto:"""

def mails_gmail (string):
    return re.findall("[a-z0-9]+[._-]?[a-z0-9]*[@][a-z]+[.]?[a-z]*",string)

print (mails_gmail ("Hola, mi correo es info@example.com. Puedes contactarme allí.facew@yahoo.comokmmerv.a-qevew@yahoo.com.arvewvewvewevw"))

def mails_yahoo (string):
         
    return re.findall("[a-z0-9]+[-._]?[@]yahoo[.][a-z]+[.]*[a-z]{2,}",string)


print (mails_yahoo ("Hola, mi correo es info@example.com. Puedes contactarme allí.facew@yahoo.comokmmerv.a-qevew@yahoo.com.arvewvewvewevw"))