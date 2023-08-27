import tv
class Control:
    def __init__(self,tv):
        self.tv=tv
        tv.setcontrol(self)
    def turnOff(self):
        self.tv.turnOff
    def turnOn(self):
        self.tv.turnOn
    def canalUp(self):
        if self.tv._estado:
            self.tv.canalUp()
    def canalDown(self):
        if self.tv._estado:
            self.tv.canalDown()
    def volumenUp(self):
        if self.tv._estado:
            self.tv.volumenUp()
    def volumenDown(self):
        if self.tv._estado:
            self.tv.volumenDown()
    def setCanal(self,nuevoCanal):
        tv.setCanal=nuevoCanal
    def setVolumen(self,nuevoVolumen):
        tv.setVolumen=nuevoVolumen
    def setTv(self,tv):
        self._tv=tv
    def getTv(self,tv):
        return tv