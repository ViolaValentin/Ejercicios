import requests

#https://pokeapi.co/api/v2/pokemon/pikachu

#1)estamos consultando el dominio pokeapi.co
#2)
"""respuesta=requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
print (respuesta.status_code)
print (respuesta.headers ["Content-Type"])

datos=respuesta.json()
print (datos["forms"])"""

pokemones=requests.get("https://pokeapi.co/api/v2/pokemon")
datos_pokemones=pokemones.json()
print (datos_pokemones ["count"])

#4 https://pokeapi.co/api/v2/pokemon/abilities
# https://pokeapi.co/api/v2/pokemon/abilities/2

pidgey=requests.get("https://pokeapi.co/api/v2/pokemon/16/")
datos_pidgey=pidgey.json()
datos_pidgeyStr="\n".join(datos_pidgey)

rattata=requests.get("https://pokeapi.co/api/v2/pokemon/19/")
datos_rattata=rattata.json()
datos_rattataStr="\n".join(datos_rattata)
with open ("ficha_tecnica_pokemons.txt","a") as arch:
    arch.write (datos_pidgeyStr),"\n", arch.write(datos_rattataStr)