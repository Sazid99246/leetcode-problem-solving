from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        result = []
        for n in nums:
            sum += n
            result.append(sum)
        return result

sol = Solution()

nums1 = [1,2,3,4]
print(sol.runningSum(nums1))
nums2 = [1,1,1,1,1]
print(sol.runningSum(nums2))