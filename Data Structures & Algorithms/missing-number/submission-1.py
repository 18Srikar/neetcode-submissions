class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        bag={}
        for each in nums:
            bag[each]=1
        for i in range(len(nums)+1):
            if i not in bag:
                return i