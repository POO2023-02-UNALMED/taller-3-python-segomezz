
from .tv import TV
class Control:
    def __init__(self):
        self.tv = None 
    def enlazar(self,tv):
        self.tv=tv
        self.tv.setControl(self)

    def turnOff(self):
        self.tv.turnOff()
    def turnOn(self):
        self.tv.turnOn()
    def canalUp(self):
        if self.tv.getEstado():
            self.tv.canalUp()
    def canalDown(self):
        if self.tv.getEstado():
            self.tv.canalDown()
    def volumenUp(self):
        if self.tv.getEstado():
            self.tv.volumenUp()
    def volumenDown(self):
        if self.tv.getEstado():
            self.tv.volumenDown()
    def setCanal(self,nuevoCanal):
        self.tv.setCanal(nuevoCanal)
    def setVolumen(self,nuevoVolumen):
        self.tv.setVolumen(nuevoVolumen)
    def setTv(self,tv):
        self.tv=tv
    def getTv(self):
        return self.tv