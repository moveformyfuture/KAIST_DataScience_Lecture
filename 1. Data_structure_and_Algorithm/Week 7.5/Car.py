

class Car:

    def __init__(self,intY,intX,strID,intSize,intOrient):
        self.intX = intX
        self.intY = intY
        self.intSize = intSize
        self.strID = strID
        self.intOrient = intOrient

    def moveDown(self,objState):
        if self.intOrient == 1:
            return False

        if objState.getSpotInfo(self.intX,self.intY+self.intSize) == '':
            self.intY = self.intY + 1
            objState.markCar(self)
            return True
        else:
            return False

    def moveUp(self, objState):
        if self.intOrient == 1:
            return False

        if objState.getSpotInfo(self.intX, self.intY - 1) == '':
            self.intY = self.intY - 1
            objState.markCar(self)
            return True
        else:
            return False

    def moveRight(self, objState):
        if self.intOrient == 0:
            return False

        if objState.getSpotInfo(self.intX + self.intSize, self.intY) == '':
            self.intX = self.intX + 1
            objState.markCar(self)
            return True
        else:
            return False

    def moveLeft(self, objState):
        if self.intOrient == 0:
            return False

        if objState.getSpotInfo(self.intX - 1, self.intY) == '':
            self.intX = self.intX - 1
            objState.markCar(self)
            return True
        else:
            return False

    def __str__(self):
        strRet = "Car "+self.strID+" : ("+str(self.intY)+","+ \
                 str(self.intX)+"), size : "+str(self.intSize)+ \
                 ", intOrient : "+str(self.intOrient)
        return strRet