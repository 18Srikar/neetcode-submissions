class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bag=set()
        for each in nums:
            if each in bag:
                return True
            else:
                bag.add(each)
        return False
        