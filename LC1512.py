class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for key in freq:
            count = freq[key] * (freq[key] - 1) // 2
            ans += count
        return ans
