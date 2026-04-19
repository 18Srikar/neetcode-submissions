class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=0
        digits.reverse()
        digits[0]+=1
        for i in range(len(digits)):
            digits[i] += carry
            carry=0
            if digits[i]>9:
                digits[i]%=10
                carry=1
        if carry==1:
            digits.append(1)
        digits.reverse()
        return digits