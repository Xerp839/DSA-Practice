class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = nums[i+1]
            if num1 + num2 == target:
                return [i, i+1]
        return []

    