#pacman rosa, verde, naranja y rojo
#comen bolitas y fantasmas
#tienen una velocidad y una cantidad de vidas (3)

class PacmanRosa ():
    def __init__(self,su_velocidad):
        self.vidas=3
        self.velocidad=su_velocidad

    def comer_bolitas (self,bolitas):
        self.velocidad+=bolitas
    
    def comer_fantasmas (self):
        self.velocidad+=8

    def toca_fantasma (self):
        self.vidas-=1

    def toca_fantasma_aleatorio (self):
        self.vidas-=2

    def morir (self):
        return self.vidas==0

    def vida_extra (self):
        if self.puntos>200:
            self.vidas+=1

    def suma_puntos (self,q_puntos):
        self.velocidad +=q_puntos*1.01

class PacmanVerde ():
    def __init__(self,su_velocidad):
        self.vidas=3
        self.velocidad=su_velocidad

    def comer_bolitas (self,bolitas):
        self.velocidad+=bolitas
    
    def comer_fantasmas (self):
        self.velocidad+=6

    def toca_fantasma (self):
        self.vidas-=1

    def toca_fantasma_aleatorio (self):
        self.vidas-=2

    def morir (self):
        return self.vidas==0

    def vida_extra (self):
        if self.puntos>200:
            self.vidas+=1

    def suma_puntos (self,q_puntos):
        self.velocidad +=q_puntos*1.01

class PacmanNaranja ():
    def __init__(self,su_velocidad):
        self.vidas=3
        self.velocidad=su_velocidad

    def comer_bolitas (self,bolitas):
        self.velocidad+=bolitas
    
    def comer_fantasmas (self):
        self.velocidad+=4

    def toca_fantasma (self):
        self.vidas-=1

    def toca_fantasma_aleatorio (self):
        self.vidas-=2

    def morir (self):
        return self.vidas==0
    
    def vida_extra (self):
        if self.puntos>200:
            self.vidas+=1

    def suma_puntos (self,q_puntos):
        self.velocidad +=q_puntos*1.01

class PacmanRojo ():
    def __init__(self,su_velocidad):
        self.vidas=3
        self.velocidad=su_velocidad
        self.puntos=0
    def comer_bolitas (self,bolitas):
        self.velocidad+=bolitas
    
    def comer_fantasmas (self):
        self.velocidad+=2

    def toca_fantasma (self):
        self.vidas-=1

    def toca_fantasma_aleatorio (self):
        self.vidas-=2

    def morir (self):
        return self.vidas==0
    
    def vida_extra (self):
        if self.puntos>200:
            self.vidas+=1

    def suma_puntos (self,q_puntos):
        self.velocidad +=q_puntos*1.01


pacmancitorosa=PacmanRosa (1)
pacmancitonaranja=PacmanNaranja (1)
pacmancitorojo=PacmanRojo (1)
pacmancitoverde=PacmanVerde (1)

print (pacmancitonaranja.comer_bolitas(60))
print (pacmancitonaranja.velocidad)
print (pacmancitonaranja.comer_fantasmas())
print (pacmancitonaranja.velocidad)