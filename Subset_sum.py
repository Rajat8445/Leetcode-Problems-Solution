class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i  # Store index of the current number
        return []
print(Solution().twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]    
