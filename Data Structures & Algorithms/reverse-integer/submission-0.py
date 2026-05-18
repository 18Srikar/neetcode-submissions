class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
            x*=-1
        temp=str(x)[::-1]
        ans=int(temp)*sign
        if ans < -2**31 or ans > (2**31) - 1:
            return 0
        return ans
        