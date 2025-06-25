from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = []
        odd = []
        for n in nums:
            if n % 2 == 0:
                even.append(n)
            else:
                odd.append(n)
        result = even + odd
        return result

s = Solution()
print(s.sortArrayByParity([3,1,2,4]))
