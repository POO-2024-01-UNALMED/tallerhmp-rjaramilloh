from deportista import Deportista
from persona import Persona

class Futbolista(Persona,Deportista):

    listaFutbolistas = []

    def __init__(self, nombre= None, edad= None, altura= None, sexo= None, añosPracticando= None,golesMarcados= None,tarjetasRojas= None,piernaHabil= None ):
        Deportista.__inint__(self,añosPracticando)
        Persona.__init__(self,nombre,edad,altura,sexo)
        self._golesMarcados=golesMarcados
        self._tarjetasRojas=tarjetasRojas
        self._piernaHabil=piernaHabil
        list.append(self)
    
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados=golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas=tarjetasRojas

    def getPiernaHabil(self):
        return self._piernaHabil
    
    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil=piernaHabil

    def __str__(self):
        return f"Mi nombre es {self._nombre} soy profesional en el deporte {self._deporte} tengo {self._edad} años de edad y llevo {self._añosPracticando} años practicando"
    
