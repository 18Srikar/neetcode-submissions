class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        bag={}
        for i in range(len(numbers)):
            if numbers[i] not in bag:
                bag[numbers[i]]=-1
            bag[numbers[i]]=i
        for i in range(len(numbers)):
            if target-numbers[i] in bag:
                ans=sorted([i+1,bag[target-numbers[i]]+1])
                return ans
        