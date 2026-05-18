class Solution:
    def countBits(self, n: int) -> List[int]:
        x=[]
        for i in range(n+1):
            x.append(bin(i)[2:])
        for i in range(len(x)):
            count=0
            for each_char in x[i]:
                if each_char=="1":
                    count+=1
            x[i]=count
        return x

            
        