
class TV:
    numTV=0
    def __init__(self,Marca,estado):
        self._Marca=Marca
        self._canal=1
        self._precio=500
        self._estado=estado
        self._volumen=1
        self._control=None
        TV.numTV+=1
    @classmethod
    def getNumTV(cls):
        return cls.numTV  
    @classmethod 
    def setNombre(cls,numTV):
        cls.numTV=numTV
    def setMarca(self,Marca):
       self._Marca=Marca 
    def getMarca(self):
        return self._Marca
    def getEstado(self):
        return self._estado
    def setCanal(self,canal):
        if 1<=canal<=120 and self._estado:
            self._canal=canal
    def getCanal(self):
        return self._canal
    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    def setVolumen(self,volumen):
        if 0<= volumen <=7 and self._estado:
            self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    def setControl(self,control):
        self._control=control
    def getControl(self):
        return self._control
    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False
    def canalUp(self):
        if 1<=self._canal<120 and self._estado:
            self._canal+=1
            return self._canal
    def canalDown(self):
        if 1<self._canal<=120 and self._estado:
            self._canal-=1
            return self._canal
    def volumenUp(self):
        if 0<=self._volumen<7 and self._estado:
            self._volumen+=1
            return self._volumen
    def volumenDown(self):
        if 0<self._canal<=7 and self._estado:
            self._volumen-=1
            return self._volumen    