class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count=1
        counts=[]
        if not nums:
            return 0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            elif nums[i]==nums[i+1]-1:
                count+=1
            else:
                counts.append(count)
                count=1
        counts.append(count)
        return max(counts)
