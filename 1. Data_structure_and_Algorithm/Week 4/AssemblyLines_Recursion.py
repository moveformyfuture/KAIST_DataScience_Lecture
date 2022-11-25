class Assemblyines : 
    # 그래프 값
    timeStation = [[7, 9, 3, 4, 8,4], [8, 5, 6, 4, 5, 7]]
    timeBelt = [[2,2,3,1,3,4,3], [4,2,1,2,2,1,2]]
    
    # memoization table 설정
    timeScheduling = [list(range(6)), list(range(6))]
    statingTracing = [list(range(6)), list(range(6))]
    
    # (1) 재귀함수 정의
    def scheduling(self, idxLine, idxStation) : 
        print("Calulate scheduling : line, station : ", idxLine, idxStation) # "(", self.intCount, "recursion calls )")
        #self.intCount = self.intCount + 1
        
        # (2) Escape Routine 설정
        if idxStation == 0 : 
            if idxLine == 1 : 
                return self.timeBelt[0][0] + self.timeStation[0][0]
            elif idxLine == 2 : 
                return self.timeBelt[1][0] + self.timeStation[1][0]
        
        # (3) 재귀문 수행
        if idxLine == 1 : 
            costLine1 = self.scheduling(1, idxStation-1) + self.timeStation[0][idxStation]
            costLine2 = self.scheduling(2, idxStation-1) + self.timeStation[0][idxStation] + self.timeBelt[1][idxStation]
        elif idxLine == 2:
            costLine1 = self.scheduling(1, idxStation-1) + self.timeStation[1][idxStation] + self.timeBelt[0][idxStation]
            costLine2 = self.scheduling(2, idxStation-1) + self.timeStation[1][idxStation]
        
        # (4) 최종 결과값 비교
        if costLine1 > costLine2 : 
            return costLine2
        else : 
            return costLine1
    
    def startScheduling(self) : 
        numStation = len(self.timeStation[0])
        costLine1 = self.scheduling(1, numStation - 1) + self.timeBelt[0][numStation]
        costLine2 = self.scheduling(2, numStation - 1) + self.timeBelt[1][numStation]
        if costLine1 > costLine2 : 
            return costLine2
        else : 
            return costLine1

lines = Assemblyines()
time, lineTracing = lines.startScheduling()
print("Fastest production time : ", time)