class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if nums[i] in d:
                return [d[nums[i]], i]
            else:
                d[find] = i
