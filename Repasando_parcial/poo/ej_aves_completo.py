"""Definí una clase de gorriones, de los cuales nos 
interesa conocer dos medidas conocidas como CSS 
(coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). 
El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza 
a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división 
pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más 
comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. 
Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su 
CSS está entre 0.5 y 2."""

class Ornitologo:
    def __init__(self):
        self.aves=[]
    def aves_en_estudio (self):
        return self.aves
    def hacer_rutina(self):
        for ave in self.aves:
            ave.comer(80)
        for ave in self.aves:
            ave.volar(70)
        for ave in self.aves:
            ave.comer(10)
    def estudiar_ave(self,ave):
        self.aves.append(ave)
        
    def aves_en_equilibrio (self):
         return [self.aves[i].esta_en_equilibrio() for i in range (len(self.aves))]
class Gorriones:
    def __init__(self):
        self.mayor_vuelo=0
        self.mayor_comida=0
        self.vuelos_registrados=0
        self.comidas_registradas=0
        self.comida_historica=0
        self.vuelo_historico=0
#metodos CSS, CSSP y CSSV. Son metodos poruqe el ej nos dice que queremos conocerlos
    def comer (self,gramos):
        if gramos>self.mayor_comida:
            self.mayor_comida=gramos
        self.comidas_registradas+=1
        self.comida_historica+=gramos
    def volar (self,km):
        if km>self.mayor_vuelo:
            self.mayor_vuelo=km
        self.vuelos_registrados+=1
        self.vuelo_historico+=km
    def CSS (self):
        try:
            return self.vuelo_historico/self.comida_historica
        except ZeroDivisionError:
            return None
    def CSSP (self):
        try:
            return self.mayor_vuelo/self.mayor_comida
        except ZeroDivisionError:
            return None
    def CSSV (self):
        try:
            return self.vuelos_registrados/self.comidas_registradas
        except ZeroDivisionError:
            return None
    def esta_en_equilibrio (self):
        if self.CSS() is not None:
          return (0.5<=self.CSS()<=2)
        else:
            False
            
class Golondrina:
    def __init__(self, energia):
        self.energia = energia

    def comer(self, gramos):
        self.energia += 4 * gramos

    def volar_en_circulos(self):
        self.volar(0)

    def volar(self, kms):
        self.energia -= 10 + kms

    def esta_en_equilibrio (self):
        return 150<=self.energia<=300

toki=Gorriones()
toki.volar(100)
print (toki.CSSV())
toki.comer(51)
print (toki.CSS())
print (toki.CSSV())
print (toki.CSSP())
print (toki.esta_en_equilibrio())

pepita=Golondrina(70)
print (pepita.esta_en_equilibrio())

ivo=Ornitologo()
ivo.estudiar_ave(pepita)
ivo.estudiar_ave (toki)
print (ivo.aves_en_estudio())
print (ivo.aves_en_equilibrio())
print (ivo.hacer_rutina())
"""Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. 
Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300."""