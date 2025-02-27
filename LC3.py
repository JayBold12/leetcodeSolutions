class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 1
        count = 1
        if len(s) < 2:
            return len(s)
        else:
            d = set(s[l])
            while r < len(s):
                if s[r] not in d:
                    d.add(s[r])
                    count = max(count, len(d))
                    r += 1
                else:
                    while s[r] in d:
                        d.remove(s[l])
                        l += 1
                    continue
        return count
