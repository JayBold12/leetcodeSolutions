class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        post = [1] * len(nums)
        ans = []
        currProd = nums[0]
        for i in range(1, len(nums)):
            pre.append(currProd)
            currProd *= nums[i]
        currProd = nums[-1]
        for i in range(-2, -len(nums)-1, -1):
            post[i] = currProd
            currProd *= nums[i]
        for i in range(len(nums)):
            ans.append(pre[i] * post[i])
        return ans
