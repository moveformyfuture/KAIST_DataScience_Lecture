from abc import *
from Car import Car
from Board import Board
import copy

class RushHourSolver:
    @abstractmethod
    def solve(self,objRushHour):
        pass

class SimpleSolver(RushHourSolver):

    # only method that you need to fill out
    # need to return two strings : carID and move direction
    # CarID : 'A', 'B', ... : the list of cars are given as "lstCar"
    # move direction : 'U' as Up, 'D' as Down, 'L' as Left, 'R' as Right
    # example:
    # return strCarID, strDirection   # strCarID='X', strDirection='R'
    def solve(self,objRushHour):
        self.printInfo(objRushHour.objBoard,objRushHour.lstCar)

        objRoot = TreeNode(None,objRushHour,'','')
        lstPastBoard = [str(objRushHour.objBoard)]
        lstQueue = [objRoot] # 1번 문제
        objSolutionTreeNode = None
        while len(lstQueue) > 0:
            objTreeNode = lstQueue[0] # 2번문제 - 첫번째꺼 방문처리 해주면 됨
            del lstQueue[0] # 3번문제 - 방문 했으므로 삭제
            lstCar = objTreeNode.objRushHour.lstCar

            for objCar in lstCar:
                for strDirection in ['U','D','L','R']:
                    objRushHourCopy = objTreeNode.objRushHour.copy()
                    if objRushHourCopy.moveCar(objCar.strID,strDirection) is not False:
                        if str(objRushHourCopy.objBoard) not in lstPastBoard:
                            objNewTreeNode = TreeNode(objTreeNode,\
                                                      objRushHourCopy,objCar.strID,strDirection)
                            objTreeNode.addChild(objNewTreeNode) # 4번 문제 - 새로운 경로를 child로 만들어줌
                            lstQueue.append(objNewTreeNode) # 5번 문제 - 새로운 경로를 큐에 추가해줌
                            lstPastBoard.append(str(objRushHourCopy.objBoard))
                            if objRushHourCopy.checkFinished() == True:
                                print("!!! Found a Solution")
                                lstQueue = []
                                objSolutionTreeNode = objNewTreeNode

        lstSolution = []
        while objSolutionTreeNode is not None:
            if objSolutionTreeNode.getParent() is not None: # 6번문제 - root가 not None 인것을 확인 = 부모 노드가 없음을 확인
                lstStep = [objSolutionTreeNode.strCarID,objSolutionTreeNode.strDirection]
                lstSolution.insert(0,lstStep)
            objSolutionTreeNode = objSolutionTreeNode.getParent() # 7번문제 - 부모 노드를 계속 찾아감! -> while문이므로 반복됨

        print(lstSolution)
        return lstSolution

    def printInfo(self,objBoard,lstCar):
        strRet = "----------------------------\n"
        strRet = strRet + "Board : \n"
        strRet = strRet + str(objBoard) + "\n"
        strRet = strRet + "Cars : \n"
        for i in range(len(lstCar)):
            strRet = strRet + str(lstCar[i]) + "\n"
        print(strRet)

class TreeNode:

    def __init__(self,objParent,objRushHour,strCarID,strDirection):
        self.objParent = objParent
        self.objRushHour = objRushHour
        self.strCarID = strCarID
        self.strDirection = strDirection
        self.lstChildren = []

    def addChild(self,objTreeNode):
        self.lstChildren.append(objTreeNode)

    def getParent(self):
        return self.objParent