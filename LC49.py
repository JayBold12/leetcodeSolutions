class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for string in strs:
            sort = "".join(sorted(string))
            if sort in d:
                d[sort].append(string)
            else:
                d[sort] = [string]
        ans = []
        for key in d:
            ans.append(d[key])
        return ans
