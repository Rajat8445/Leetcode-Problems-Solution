class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # Merge the two sorted arrays
        merged = sorted(nums1 + nums2)
        
        # Calculate the median
        n = len(merged)
        if n % 2 == 0:
            median = (merged[n // 2 - 1] + merged[n // 2]) / 2.0
        else:
            median = merged[n // 2]
        
        return median
print(Solution().findMedianSortedArrays([1, 3], [2]))  # Output: 2.0
print(Solution().findMedianSortedArrays([1, 2], [3, 4]))  # Output: 2.5