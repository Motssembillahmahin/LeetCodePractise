class Solution:
    def mySqrt(self, c: int) -> int:
        l, r = 0, c
        res = 0

        while l <= r:
            m = (l + r)//2

            if m**2 > c:
                r = m - 1
            elif m**2 < c:
                l  = m + 1
                res = m
            else:
                return m
        return res


## This part for local device testing, no need for leetcode Server
value = Solution()
print(value.mySqrt(8))