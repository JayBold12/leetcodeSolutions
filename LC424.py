class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 1
        l = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            window = r - l + 1
            mostFreq = max(freq.values())
            check = window - mostFreq
            if check <= k:
                ans = max(ans, window)
            else:
                while r - l + 1 - max(freq.values()) > k:
                    freq[s[l]] -= 1
                    l += 1
        return ans
