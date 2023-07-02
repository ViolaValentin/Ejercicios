import requests
respuesta=requests.get("https://rickandmortyapi.com/api/location")


class Guia():
    def __init__(self):
        self.residentes=[]
        self.datos=None

    def get_info_api(self):
        self.datos=requests.get ("https://rickandmortyapi.com/api/location")

    def residentes_de(self,lugar):
        self.get_info_api()
        for residente in self.datos.json()["results"]["name"==lugar]["residents"]:
            nombre_residentes=requests.get(residente).json()
            self.residentes.append(nombre_residentes["name"])

    def persistir_datos_de(self,nombre,archivo):
        respuesta = requests.get("https://rickandmortyapi.com/api/character/" + nombre)
        with open (archivo,"w") as arch_datos:
            arch_datos.write (str(respuesta.json()))
        
guiador=Guia()
guiador.persistir_datos_de("4","residente.txt")
"""
#b) El dominio al que estamos consultando es "rickandmortyapi.com"
#c)
datos=respuesta.json()
print (f"La API tiene almacenados", datos["info"]["count"], "lugares")"""

#e)
""""En la arquitectura cliente servidor, el servidor es la parte que aporta contenido, información, datos. El cliente,
es quien lo consume. Las características que posea un servidor son relativas al uso que se le de al mismo, a la 
demanda que tenga. También, debemos considerar que no necesariamente existe una diferencia en su hardaware o software
pero si en su lógica.
En este caso, el servidor aporta la información de las promociones que solicita el cliente al hacer clic en los botones."""