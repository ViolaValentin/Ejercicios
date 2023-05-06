class Titanes:
    def __init__ (self,su_salud):
        self.salud=su_salud
    #reciben daño
    #mueren
    #destruir cosas
    #grito
    def recibir_ataque (self,daño):
        self.salud-=daño*1.5
    def esta_vivo (self):
        if self.salud>0:
            return self.salud
        else:
            ("Está muerto")
    def grito (self):
        return ("¡Aaaarrrg!")
    def cuantas_casas (self):
        cuantas_casas=((self.salud*8)/100)
        return cuantas_casas
    def destruir_casas (self):
        return self.salud==(self.cuantas_casas()//1)*12.5
    

titan1 = Titanes(100)
titan1.recibir_ataque(30)
print(titan1.esta_vivo())
print(titan1.esta_vivo())
print(titan1.cuantas_casas())
print(titan1.grito())
titan1.destruir_casas()
titan1.esta_vivo()
titan1.recibir_ataque(4)
print(titan1.esta_vivo())


