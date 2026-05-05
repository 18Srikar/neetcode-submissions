class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_cnt = 1, 0
        output=[]
        for num in nums:
            if num:
                prod *= num
            else:
                zero_cnt +=  1
        if zero_cnt > 1: return [0] * len(nums)
        if zero_cnt==1: 
            for i in range(len(nums)):
                if nums[i]==0:
                    output.append(prod)
                else:
                    output.append(0)
        else:
            for i in range(len(nums)):
                output.append(prod//nums[i])
        return output