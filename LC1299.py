class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        high = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = high
            high = max(high, curr)
        return arr
