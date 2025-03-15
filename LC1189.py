class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ans = 0
        word = {"b": 1,
        "a" : 1,
        "l" : 2,
        "o" : 2,
        "n" : 1}
        freq = {}
        for char in text:
            freq[char] = 1 + freq.get(char, 0)
        spelled = True
        while spelled:
            for key in word:
                if key in freq and freq[key] >= word[key]:
                    freq[key] -= word[key]
                else:
                    spelled = False
                    break
            if spelled:
                ans += 1
        return ans
