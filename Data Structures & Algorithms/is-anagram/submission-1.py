class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        bag1={}
        bag2={}
        for each in s:
            if each in bag1:
                bag1[each]+=1
            else:
                bag1[each]=1
        for each in t:
            if each in bag2:
                bag2[each]+=1
            else:
                bag2[each]=1
        if bag1==bag2:
            return True
        return False
        