class Assemblyines : 
    # 그래프 값
    timeStation = [[7, 9, 3, 4, 8,4], [8, 5, 6, 4, 5, 7]]
    timeBelt = [[2,2,3,1,3,4,3], [4,2,1,2,2,1,2]]
    
    # memoization table 설정
    timeScheduling = [list(range(6)), list(range(6))]
    stationgTracing = [list(range(6)), list(range(6))]
    
    def startSchedulingDP(self) : 
        # 초기 값 세팅
        numStation = len(self.timeStation[0])
        self.timeScheduling[0][0] = self.timeStation[0][0] + self.timeBelt[0][0] # 9
        self.timeScheduling[1][0] = self.timeStation[1][0] + self.timeBelt[1][0] # 12
        
        # station 다 돌때까지
        for itr in range(1, numStation) : 
            # 방문 처리 (4가지 방법 존재)
            if self.timeScheduling[0][itr-1] > self.timeScheduling[1][itr-1] + self.timeBelt[1][itr] : 
                self.timeScheduling[0][itr] = self.timeStation[0][itr] + self.timeScheduling[1][itr-1] + self.timeBelt[1][itr]
                self.stationgTracing[0][itr] = 1
            else : 
                self.timeScheduling[0][itr] = self.timeStation[0][itr] + self.timeScheduling[0][itr-1]
                self.stationgTracing[0][itr] = 0
            
            if self.timeScheduling[1][itr-1] > self.timeScheduling[0][itr-1] + self.timeBelt[0][itr] : 
                self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[0][itr-1] + self.timeBelt[0][itr]
                self.stationgTracing[1][itr] = 0
            else : 
                self.timeScheduling[1][itr] = self.timeStation[1][itr] + self.timeScheduling[1][itr-1]
                self.stationgTracing[1][itr] = 1
        
        # 마지막 값 계산
        costLine1 = self.timeScheduling[0][numStation-1] + self.timeBelt[0][numStation]
        costLine2 = self.timeScheduling[1][numStation-1] + self.timeBelt[1][numStation]
        
        if costLine1 > costLine2 : 
            return costLine2, 1
        else : 
            return costLine1, 0

    def printTracing(self, lineTracing) : 
        numStation = len(self.timeStation[0])
        print("Line : ", lineTracing, "Station : ", numStation)
        for itr in range(numStation-1, 0, -1) : 
            lineTracing = self.stationgTracing[lineTracing][itr]
            print("Line : ", lineTracing, "Station : ", itr)

lines = Assemblyines()
time, lineTracing = lines.startSchedulingDP()
print("Fastest production time : ", time)
lines.printTracing(lineTracing)