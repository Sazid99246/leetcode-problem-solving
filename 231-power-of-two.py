class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

s = Solution()
print(s.isPowerOfTwo(1))
print(s.isPowerOfTwo(16))
print(s.isPowerOfTwo(3))