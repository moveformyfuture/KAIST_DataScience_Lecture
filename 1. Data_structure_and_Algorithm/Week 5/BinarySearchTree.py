import queue
import TreeNode

class TreeNode :
    nodeLHS = None
    nodeRHS = None
    nodeParent = None
    value = None
    
    def __init__(self, value, nodeParent) : 
        self.value = value
        self.nodeParent = nodeParent
        
    def getLHS(self) : 
        return self.nodeLHS
        
    def getRHS(self) : 
        return self.nodeRHS
    
    def getValue(self) : 
        return self.value
    
    def getParent(self) :
        return self.nodeParent
    
    def setLHS(self, LHS) : 
        self.nodeLHS = LHS
        
    def setRHS(self, RHS) : 
        self.nodeRHS = RHS
        
    def setValue(self, value) : 
        self.value = value
        
    def setParent(self, nodeParent) : 
        self.nodeParent = nodeParent

class BinarySearchTree : 
    # Root에 대해서만 refernece 저장
    # Root에서 traverse 수행
    root = None
    
    def __init__(self) : 
        pass
    
    def insert(self, value, node = None):
        if node is None : 
            node = self.root
        
        # 재귀함수 Escape Routine
        if self.root is None : # root 셋팅
            self.root = TreeNode(value, None)
            return
        if value == node.getValue() : # 기존값 == 삽입 값
            return
        
        
        # 하위노드를 root로 보고 연산 수행
        if value > node.getValue() : # 삽입갓 > 기존값
            if node.getRHS() is None :
                node.setRHS(TreeNode(value, node)) 
            else : 
                self.insert(value, node.getRHS())
        
        if value < node.getValue() : # 삽입값 < 기존값
            if node.getLHS() is None : 
                node.setLHS(TreeNode(value, node))
            else : 
                self.insert(value, node.getLHS())
        return
    
    def search(self, value, node = None) : 
        if node is None : 
            node = self.root
        
        # escape routine
        if value == node.getValue() : # 기존값 == 탐색 값
            return True
        
        if value > node.getValue() : # 탑색값 > 기존값
            if node.getRHS() is None : 
                return False
            else : 
                return self.search(value, node.getRHS())
        if value < node.getValue() : # 탐색값 < 기존값
            if node.get_LHS() is None : 
                return False
            else : 
                return self.search(value, node.getLHS())
            
    def delete(self, value, node = None) : 
        if node is None :
            node = self.root
        
        # 재귀함수 escape문
        if node.getValue() < value : 
            return self.delete(value, node.getRHS())
        
        
        # root를 삭제하려는 경우
        if node.getValue == value :
            
            # LHS와 RHS가 존재하는 경우 : root와 RHS의 최솟값을 교체
            if node.getLHS() is not None and node.getRHS() is not None : 
                nodeMin = self.findMin(node.getRHS()) 
                node.setValue(nodeMin.getValue())
                self.delete(nodeMin.getValue(), node.getRHS())
                return
            parent = node.getParent()
            
            # LHS만 존재하는 경우
            if node.getLHS() is not None : 
                if node == self.root :
                    self.root = node.getLHS()
                elif parent.getLHS() == node : 
                    parent.setLHS(node.getLHS())
                    node.getLHS().setParent(parent)
                else : 
                    parent.setRHS(node.getLHS())
                    node.getLHS().setParent(parent)
                return
            
            # RHS만 존재하는 경우
            if node.getRHS() is not None : 
                if node == self.root : 
                    self.root = node.getRHS()
                elif parent.getLHS() == node :
                    parent.setLHS(node.getRHS())
                    node.getRHS().setParent(parent) 
                else : 
                    parent.setRHS(node.retRHS())
                    node.getRHS().setParent(parent)
                return
            
            # LHS와 RHS 모두 없는 경우
            if node == self.root : 
                self.root = None
            elif parent.getLHS() == node : 
                parent.setLHS(None)
            else : 
                parent.setRHS(None)
            return
    
    # 최댓값 찾기(재귀함수)
    def findMax(self, node = None) : 
        if node is None : 
            node = self.root
        if node.getRHS() is None : 
            return node
        return self.findMax(node.getRHS())
    
    # 최솟값 찾기(재귀함수)
    def findMin(self, node = None) : 
        if node is None : 
            node = self.root
        if node.getLHS() is None :
            return node
        return self.findMin(node.getLHS())
    
    # BFS 방식
    def traverseLevelOrder(self) : 
        ret = []
        Q = queue()
        Q.enqueue(self.root)
        while not Q.isEmpty() : 
            node = Q.dequeue()
            if node is None : 
                continue
            ret.append(node.getValue())
            if node.getLHS() is not None : 
                Q.enqueue(node.getLHS())
            if node.getRHS() is not None :
                Q.enqueue(node.getRHS())
        return ret
    
    # DFS - in order 방식 / 순서 : LHS, 현재, RHS 순서
    def traverseInOrder(self, node = None) : 
        # escape
        if node is None :
            node = self.root
        ret = []
        if node.getLHS() is not None : 
            ret = ret + self.traverseInOrder(node.getLHS())
        ret.append(node.getValue()) # 해당 코드의 순서에 따라 구분
        if node.getRHS() is not None : 
            ret = ret + self.traverseInOrder(node.getRHS())
        return ret
    
    # DFS - pre order 방식 / 순서 : 현재, LHS, RHS 순서
    def traversePreOrder(self, node = None) : 
        if node is None : 
            node = self.root    
        ret = []
        ret.append(node.getValue()) # 해당 코드의 순서에 따라 구분
        if node.getLHS() is not None : 
            ret = ret + self.traversePreOrder(node.getLHS())
        if node.getRHS() is not None : 
            ret = ret + self.traversePreOrder(node.getRHS())
        return ret
    
    # DFS - post order 방식 / 순서 : LHS, RHS, 현재 순서
    def traversePostOrder(self, node = None) : 
        if node is None : 
            node = self.root
        ret = []
        if node.getLHS() is not None : 
            ret = ret + self.traversePostOrder(node.getLHS())
        if node.getRHS() is not None : 
            ret = ret + self.traversePostOrder(node.getRHS())
        ret.append(node.getValue()) # 해당 코드의 순서에 따라 구분
        return ret
    
tree = BinarySearchTree()
tree.insert(3)
tree.insert(2)
tree.insert(0)
tree.insert(5)
tree.insert(7)
tree.insert(4)
tree.insert(6)
tree.insert(1)
tree.insert(9)
tree.insert(8)
print(tree.traverseInOrder())

tree.delete(5)
print(tree.traverseInOrder())
                    