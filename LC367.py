class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l = 1
        r = num
        while l < r:
            m = (l+r) // 2
            if m**2 == num:
                return True
            if m**2 > num:
                r = m - 1
            if m**2 < num:
                l = m + 1
        return l**2 == num
