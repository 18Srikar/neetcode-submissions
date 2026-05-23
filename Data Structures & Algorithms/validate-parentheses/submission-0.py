class Solution:
    def isValid(self, s: str) -> bool:
        bag={"(":")","{":"}","[":"]"}
        l=0
        stack=[]
        for each in s:
            if each in bag:
                stack.append(each)
            else:
                if not stack or bag[stack[-1]]!=each:
                    return False
                stack.pop()
        return not stack



