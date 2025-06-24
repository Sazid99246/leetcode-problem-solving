class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start filling from the end
        i = m - 1  # Last index of the actual elements in nums1
        j = n - 1  # Last index in nums2
        k = m + n - 1  # Last index in nums1 (includes extra space)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 is not exhausted (nums1 is already in place)
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
