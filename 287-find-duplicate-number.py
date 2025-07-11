from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the intersection
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))
print(s.findDuplicate([3, 1, 3, 4, 2]))
print(s.findDuplicate([3, 3, 3, 3, 3]))
