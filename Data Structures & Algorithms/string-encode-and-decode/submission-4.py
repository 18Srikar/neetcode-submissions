class Solution:

    def encode(self, strs: List[str]) -> str:
        sizes=[]
        if not strs:
            return ""
        for each in strs:
            sizes.append(str(len(each)))
        ans=",".join(sizes)
        ans+="#"
        ans+="".join(strs)
        return ans
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        key,msg=s.split('#',1)
        keyvals=key.split(",")
        ans=[]
        x=0
        for each in keyvals:
            ans.append(msg[x:x+int(each)])
            x+=int(each)
        return ans

        

        

        