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
    def cazar(self):
        self.velocidad = 2
    def mover(self):
        self.energia -= 10
        if self.energia <= 0:
            self.energia = 0
    def envejecer(self):
        self.edad+=1
        if self.edad >= 40:
            self.vida = 0
    def matar(self, presa):
        presa.vida = 0
        if self.energia < 100:
            self.energia+= presa.energia * 0,10
            
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
        for k in range(self.columnas-1):
            for j in range(self.filas-1):
                if self.espacio[k][j] != 'x':
                    if self.espacio[k][j].dieta == "Carnivoro":
                        for r in range(1,self.espacio[k][j].rango+1):
                            if k + r >= self.columnas-1:
                                r = (k+r)-(self.columnas-1) 
                            if self.espacio[k+r][j] !='x' and self.espacio[k+r][j].dieta == "Herviboro":
                                l= k-r-1
                                self.espacio[k][j].cazar()
                                v= self.espacio[k][j].velocidad
                                if l-v == 1:
                                    v = 1
                                self.espacio[k-v][j] = self.espacio[k][j]
                                self.espacio[k][j] = 'x'
                                if self.espacio[k-l][j] == 0:
                                   self.espacio[k-l][j].matar(self.espacio[k-l+1][j])                              
                            elif self.espacio[k+r][j] !='x' and self.espacio[k][j+r].dieta == "Herviboro":
                                l= j-r-1
                                self.espacio[k][j].cazar()
                                v= self.espacio[k][j].velocidad
                                if l-v == 1:
                                    v = 1
                                self.espacio[k][j-v] = self.espacio[k][j]
                                self.espacio[k][j] = 'x'
                                if self.espacio[k][j-l] == 0:
                                   self.espacio[k][j-l].matar(self.espacio[k][j-l+1])                                
                            # elif self.espacio[k+r][j+r].dieta == "Herviboro":
                            # elif self.espacio[k+r][j-r].dieta == "Herviboro":
                            # elif self.espacio[k-r][j].dieta == "Herviboro":
                            # elif self.espacio[k-r][j-r].dieta == "Herviboro":
                            # elif self.espacio[k-r][j+r].dieta == "Herviboro":
                            # elif self.espacio[k][j-r].dieta == "Herviboro":       
animal1= animal(100, 100, 1,'Le', "Leon",'Carnivoro',2)
animal3= animal(100, 100, 1,'Gac', "Gacela",'Herviboro',2)

animales= [animal1,animal3]
ecosistema1= ecosistema(10,10)
ecosistema1.agregar(animal1)
ecosistema1.agregar(animal3)
while True:
     ecosistema1.mover()
     ecosistema1.mostrar()
     ecosistema1.cazar()
     x=input()
    
                            