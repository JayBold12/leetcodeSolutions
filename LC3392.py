class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        l = 0
        r = 2
        while r < len(nums):
            if nums[l] + nums[r] == nums[l+1] / 2:
                count += 1
            l += 1
            r += 1
        return count
