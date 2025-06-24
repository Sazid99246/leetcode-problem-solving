from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == 2 * arr[j]:
                        return True
        return False


s = Solution()
print(s.checkIfExist([10, 2, 5, 3]))
print(s.checkIfExist([3, 1, 7, 11]))
