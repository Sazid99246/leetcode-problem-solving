class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)  # Calculating the size of the array
        maximum_ones = 0  # This is our answer
        counting_one = 0  # Helps us count the total number of ones

        for i in range(n):
            if nums[i] == 1:
                counting_one += 1  # If one, count it
            else:
                counting_one = 0  # If zero, reset the count

            maximum_ones = max(maximum_ones, counting_one)  # Update max

        return maximum_ones
