class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        x=s.lower()
        for each in x:
            if each.isalnum():
                temp.append(each)
        i=0
        j=len(temp)-1
        while i<j:
            if temp[i]==temp[j]:
                i+=1
                j-=1
            else:
                return False
        return True
        print(temp,s)
