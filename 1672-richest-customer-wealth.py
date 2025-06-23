from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(account) for account in accounts)


s = Solution()
print(s.maximumWealth([[1, 5], [7, 3], [3, 5]]))
