class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = list(sorted(heights))
        match = 0
        for i in range(len(heights)):
            if heights[i] != sorted_list[i]:
                match += 1
        return match