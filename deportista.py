class Deportista():
    def __inint__(self,añosPracticando = None):
        self._deporte = "Futbol"
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte
    
    def setDeporte(self, deporte):
        self._deporte=deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando
    
    def sefAñosPracticando(self, añosPracticando):
        self._añosPracticando=añosPracticando