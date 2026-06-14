class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp=[]
        for i in range(len(temperatures)):
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    temp.append(j-i)
                    break
                if j==len(temperatures)-1:
                    temp.append(0)
        temp.append(0)    
        return temp
