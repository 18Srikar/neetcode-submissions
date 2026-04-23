class Solution:
    def hammingWeight(self, n: int) -> int:
        d=str(bin(n))[2:]
        ans=0
        for each in d:
            if each=='1':
                ans+=1
        return ans
        