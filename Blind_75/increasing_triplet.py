from math import inf


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = None
        second = None

        for i in range(len(nums)):

            if first is None:
                first = nums[i]

            elif first and second:
                if nums[i] > second:
                    return True

            else:
                if nums[i] < first

            if nums[i] < first:
                first = nums[i]
            

                



