class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        freq = {}
        for char in chars:
            freq[char] = 1 + freq.get(char, 0)
        for word in words:
            tmpFreq = {}
            for char in word:
                tmpFreq[char] = 1 + tmpFreq.get(char, 0)
            spelled = True
            for key in tmpFreq:
                if key not in freq or freq[key] < tmpFreq[key]:
                    spelled = False
                    break
            if spelled:
                ans += len(word)
        return ans
