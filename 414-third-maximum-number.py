class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_list = sorted(set(nums), reverse=True)
        if len(sorted_list) == 0:
            return 0
        elif len(sorted_list) == 1 or len(sorted_list) == 2:
            return sorted_list[0]
        else:
            return sorted_list[2]
