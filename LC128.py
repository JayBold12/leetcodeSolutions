class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        numbers = set(nums)
        for num in numbers:
            count = 0
            if num - 1 not in numbers:
                while num in numbers:
                    count += 1
                    num += 1
            ans = max(ans, count)
        return ans
