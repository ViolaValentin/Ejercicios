class Enterprise:
    def __init__(self):
        self.potencia=50
        self.coraza=5

    def encontrarPilaAtomica (self):
        if self.potencia+25<100:
            self.potencia+=25
        else:
            return self.potencia==100
    def encontrarEscudo (self):
        if self.coraza+10<=20:
            self.coraza+=10
        else:
            return self.coraza==20
    def recibirAtaque (self,ataque): 
        if ataque<=self.coraza:
            return self.coraza-ataque
        elif ataque>self.potencia+self.coraza:
            return self.potencia==0 and self.coraza==0
        elif ataque>self.coraza and ataque<self.potencia:
            descontar_potencia=self.coraza-ataque
            self.coraza=0
            return self.potencia+descontar_potencia
        
    def fortalezaDefensiva (self):
        return self.coraza+self.potencia
    def necesitaFortalecerse (self):
        return self.coraza<=0 and self.potencia<=20
    def fortalezaOfensiva (self):
        if self.potencia<20:
            return 0
        else:
            return (self.potencia - 20) / 2

enterprise = Enterprise()
print (enterprise.encontrarPilaAtomica())
print (enterprise.recibirAtaque(14))
print (enterprise.encontrarEscudo())
print (enterprise.coraza)
print (enterprise.fortalezaDefensiva())
print (enterprise.fortalezaOfensiva())
print (enterprise.necesitaFortalecerse())