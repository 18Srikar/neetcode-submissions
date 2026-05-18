class Solution:
    def reverseBits(self, n: int) -> int:
        temp=list(bin(n)[2:][::-1])
        while len(temp)<32:
            temp.append('0')
        ans="".join(temp)
        return int(ans,2)

        