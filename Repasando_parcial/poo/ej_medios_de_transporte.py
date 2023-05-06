class MedioDeTransporte():
    def __init__(self,su_combustible):
        self.medio=[]
        self.combustible=su_combustible

    def cargar_combustible(self,litros):
        self.combustible+=litros

class Moto(MedioDeTransporte): 
    def __init__ (self):
        super().__init__(su_combustible=52)
        self.capacidad=2

    def recorrer (self,km):
        self.combustible-=km
    
    def entran_personas (self,cantidad):
        return self.capacidad>=cantidad

class Auto(MedioDeTransporte):
    def __init__ (self):
        super().__init__(su_combustible=40)
        self.capacidad=5

    def recorrer (self,km):
        self.combustible-=km/2

    def entran_personas (self,cantidad):
        return self.capacidad>=cantidad
    
motito=Moto()
autito=Auto ()
medios=MedioDeTransporte(0)
print (motito.combustible)
motito.cargar_combustible(60)
print (motito.combustible)
print (autito.entran_personas(3))