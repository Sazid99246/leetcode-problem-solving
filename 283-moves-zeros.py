class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Move all 0's to the end while maintaining the relative order of the non-zero elements.
        Do not return anything, modify nums in-place instead.
        """
        non_zero_pos = 0

        # Move all non-zero elements to the beginning
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pos] = nums[i]
                non_zero_pos += 1

        # Fill the rest with zeroes
        for i in range(non_zero_pos, len(nums)):
            nums[i] = 0
