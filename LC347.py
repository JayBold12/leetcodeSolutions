class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for key in freq:
            buckets[freq[key]].append(key)
        for i in range(len(nums), 0, -1):
            if len(ans) == k:
                break
            else:
                if len(buckets[i]) > 0:
                    for n in buckets[i]:
                        if len(ans) == k:
                            break
                        else:
                            ans.append(n)
        return ans
                        
