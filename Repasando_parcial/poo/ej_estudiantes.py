class Estudiante:
    def __init__ (self,su_energia):
        self.energia=su_energia
        self.animo=False
    def energia_actual (self):
        return self.energia
    def comer (self):
        self.energia+=10
    def dormir (self,horas):
        self.energia=(horas*100)/8
    def hacer_ejercicio (self,horas):
        bloques=horas/30
        self.energia-=25*bloques
    def estudiar (self,horas):
        self.energia-=20*horas
    def aprobar (self):
        return not self.animo
estudiante = Estudiante(100)
estudiante.hacer_ejercicio(30)
estudiante.estudiar(3)
estudiante.comer()
print(estudiante.aprobar())
print(estudiante.energia_actual())