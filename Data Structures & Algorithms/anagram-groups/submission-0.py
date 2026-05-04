class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for each in strs:
            temp="".join(sorted(each))
            ans[temp].append(each)
        return list(ans.values())