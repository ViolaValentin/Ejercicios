import re
#1

string="Hola, soy una cadena y tengo 5 caracteres permitidos"
patron= "0-9"
patron2= "[A-Z]"
if re.search (patron or patron2,string):
    print ("Si! Tengo caracteres permitidos")
else:
    print ("Lo siento, no tengo caracters permitidos")