import matplotlib.pyplot as plt
import numpy as np


from PlanNode import PlanNode

class ProductionList(PlanNode):
    def __init__(self, Filename):

        self.nodeHead = PlanNode(-1, 'head', '')
        self.nodeTail = PlanNode(-1, 'tail', '')

        self.nodeHead.setNextNode(self.nodeTail)
        self.nodeTail.setPrevNode(self.nodeHead)

        if Filename != '':

            f = open(Filename)
            temp = f.readlines()
            f.close()

            dataset = []
            for row in temp:
                dataset.append(row[:-1].split(','))
            Dataset = np.asarray(dataset[1:]).T

            numNos = Dataset[0].astype('int')
            strSerialNumbers = Dataset[1].astype('str')
            strModels = Dataset[2].astype('str')
            for i in range(len(numNos)):
                node = PlanNode(numNos[i], strSerialNumbers[i], strModels[i])
                node.printOut()
                self.addLast(node)

    def addLast(self, node):
        nodeLast = self.nodeTail.getPrevNode()
        nodeLast.setNextNode(node)
        node.setPrevNode(nodeLast)
        node.setNextNode(self.nodeTail)
        self.nodeTail.setPrevNode(node)

    def addFirst(self, node):
        # Problem 1. complete the add first function of a doubly linked list
        # 'node' at the first of the linked list
        nodeFirst = self.nodeHead.getNextNode() # 기존에 Head 다음에 있던 노드인 'nodeFrist'를 만듦
        node.setNextNode(nodeFirst) # node의 다음 노드는 nodeFirst이기 위해 nextnode 경로 설정
        nodeFirst.setPrevNode(node) # nodeFirst의 이전경로 설정 -> double linked list이므로 총 2번 설정
        node.setPrevNode(self.nodeHead) # node의 이전 노드를 head로 설정
        self.nodeHead.setNextNode(node) # nodeHead의 다음 노드 설정

    def removeLast(self):
        # Problem 1. complete the remove last function of a doubly linked list
        # remove the node at the last of the linked list
        node = self.nodeTail.getPrevNode() # tail 이전에 있는 node를 생성
        if node.strSerialNumber != 'head':
            prevNode = node.getPrevNode() # node 이전에 있는 prevNode 생성
            prevNode.setNextNode(self.nodeTail) # prevNode와 Tail 연결
            self.nodeTail.setPrevNode(prevNode) # tail과 prevNode를 연결
        return node

    def removeFirst(self):
        #  Problem 1. complete the remove first function of a doubly linked list
        # remove the node at the first of the linked list
        node = self.nodeHead.getNextNode()
        if node.strSerialNumber != 'tail' : 
            nextNode = node.getNextNode()
            nextNode.setPrevNode(self.nodeHead)
            self.nodeHead.setNextNode(nextNode) # 교수님은 (node)로 풀이
        return node

    def getSize(self):
        # Problem 1. complete the code of a doubly linked list to
        # return the size of the linked list excluding head and tail nodes
        node = self.nodeHead
        cnt = 0
        while node.getNextNode().strSerialNumber != 'tail':
            node = node.getNextNode() # 교수님은 .nextNode()로 풀이
            cnt += 1
        return cnt

    def getListString(self):
        node = self.nodeHead
        ListString = ''
        while node.getNextNode().strSerialNumber != 'tail':
            node = node.getNextNode()
            ListString = ListString + ','
            ListString = ListString + str(node.numNo)
        return ListString

    def showPlanChart(self):

        allStartDate = []
        allModel = []
        node = self.nodeHead

        while node.getNextNode() != self.nodeTail:
            node = node.getNextNode()
            allStartDate.append(node.dateStart)
            allModel.append(node.strModel)

        Uniq_allModel = list(set(allModel))
        Counting_allModel = [allModel.count(a) for a in Uniq_allModel]
        xlabel = [i for i in range(len(Uniq_allModel))]
        plt.bar(xlabel[0:10], Counting_allModel[0:10], align='center')
        plt.xticks(xlabel[0:10], Uniq_allModel[0:10])
        plt.xlabel('Model')
        plt.ylabel('Number of Orders')
        plt.show()

        Uniq_allStartDate = list(set(allStartDate))
        Counting_dateStart = [allStartDate.count(a) for a in Uniq_allStartDate]
        xlabel = [i for i in range(len(Uniq_allStartDate))]
        plt.bar(xlabel[0:10], Counting_dateStart[0:10], align='center')
        plt.xticks(xlabel[0:10], Uniq_allStartDate[0:10])
        plt.xlabel('Date')
        plt.ylabel('Number of Orders')
        plt.show()