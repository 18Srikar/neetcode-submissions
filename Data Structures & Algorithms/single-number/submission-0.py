class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bag={}
        for each in nums:
            if each in bag:
                bag[each]+=1
            else:
                bag[each]=1
        for each in bag:
            if bag[each]==1:
                return each
        
        