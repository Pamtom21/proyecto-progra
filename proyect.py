import random as ra
class organismo:
    def __init__(self,vida, enegia, velocidad, icono):
        self.vida=vida
        self.energia= enegia
        self.velocidad= velocidad
        self.icono = icono
class animal(organismo):
    def __init__(self, vida, enegia, velocidad,icono, especie,dieta,rango):
        super().__init__(vida, enegia, velocidad,icono)
        self.especie= especie
        self.dieta= dieta
        self.rango= rango
        self.edad= 1
    def __str__(self) -> str:
        return f'{self.icono}'
    def cazar(self, obj):
        self.velocidad = 2
        obj.vida = 0
        if self.energia < 100:
            self.energia += obj.energia
            if self.energia > 100:
                self.energia = 100
    def mover(self):
        self.energia -= 10
        if self.energia <= 0:
            self.energia = 0
    def envejecer(self):
        self.edad+=1
        if self.edad >= 40:
            self.vida = 0
            
class planta(organismo):
    def __init__(self, vida, enegia,icono):
        super().__init__(vida, enegia,icono)
class abioticos:
    def __init__(self, icono):
        self.icono = icono
class ambiente:
    def __init__(self):
        self.abioticos=[]
class ecosistema:
    def __init__(self,filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.espacio=[['x' for x in range(self.columnas)] for y in range(self.filas)]
    def mostrar(self):
        for k in self.espacio:
            resultado= "   ".join([str(y) for y in k])
            print(resultado)
    def agregar(self, obj):
        posx = ra.randint(0,self.columnas-1)
        posy= ra.randint(0,self.filas-1)
        if self.espacio[posx][posy] == 'x':
            self.espacio[posx][posy] = obj
    def eliminar(self):
        for k in range(self.columnas):
            for j in range(self.filas):
                if self.espacio[k][j] != 'x':
                    if self.espacio[k][j].vida != 0:
                        self.espacio[k][j] = 'x'
    def mover(self):
        for k in range(self.columnas):
            for j in range(self.filas):
                if self.espacio[k][j] != 'x':
                    if self.espacio[k][j].velocidad >= 1:
                        decision=ra.randint(0,3)
                        if str(decision) == '0':#mov adelante
                            v=self.espacio[k][j].velocidad
                            if k+v <= self.columnas-1:
                                self.espacio[k+v][j] = self.espacio[k][j]
                                self.espacio[k][j] = 'x'
                        if str(decision) == '1':#mov atras
                            v=self.espacio[k][j].velocidad
                            if k-v >= 0:
                                self.espacio[k-v][j] = self.espacio[k][j]
                                self.espacio[k][j] = 'x'
                        if str(decision) == '2':#mov derecha
                            v=self.espacio[k][j].velocidad
                            if j+v <= self.filas-1:
                                self.espacio[k][j+v] = self.espacio[k][j]
                                self.espacio[k][j] = 'x'
                        if str(decision) == '3':#mov derecha
                            v=self.espacio[k][j].velocidad
                            if j-v >= 0:
                                self.espacio[k][j-v] = self.espacio[k][j]
                                self.espacio[k][j] = 'x'
    def cazar(self):
        for k in range(self.columnas):
            for j in range(self.filas):
                if self.espacio[k][j] != 'x':
                    if self.espacio[k][j].dieta == "Carnivoro":
                        for r in range(1,self.espacio[k][j].rango+1):
                            if self.espacio[k+r][j].dieta == "Herviboro" or self.espacio[k][j+r].dieta == "Herviboro" or self.espacio[k+r][j+r].dieta == "Herviboro" or self.espacio[k+r][j-r].dieta == "Herviboro" or self.espacio[k-r][j].dieta == "Herviboro" or self.espacio[k-r][j-r].dieta == "Herviboro" or self.espacio[k-r][j+r].dieta == "Herviboro"  or self.espacio[k][j-r].dieta == "Herviboro": 
                                    
animal1= animal(100, 100, 1,'L', "Leon",'Carnivoro',2)
animal2= animal(100, 100, 1,'K', "Leon",'Carnivoro',2)
animal3= animal(100, 100, 1,'J', "Leon",'Carnivoro',2)
animal4= animal(100, 100, 1,'M', "Leon",'Carnivoro',2)
animales= [animal1,animal2,animal3,animal4]
ecosistema1= ecosistema(10,10)
while True:
     var= ra.randint(0,3)
     ecosistema1.agregar(animales[var])
     ecosistema1.mover()
     ecosistema1.mostrar()
     x=input()
    
                            