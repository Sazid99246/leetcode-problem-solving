class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = sorted(list(map(lambda x: x**2, nums)))
        return result
