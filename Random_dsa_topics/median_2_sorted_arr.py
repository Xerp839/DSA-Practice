class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = 0
        r = 0
        merged_arr = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] < nums2[r]:
                merged_arr.append(nums1[l])
                l += 1
            else:
                merged_arr.append(nums2[r])
                r += 1
        
        while l < len(nums1):
            merged_arr.append(nums1[l])
            l += 1
        
        while r < len(nums2):
            merged_arr.append(nums2[r])
            r += 1
        
        x = len(merged_arr)
        y = x/2

        if len(merged_arr) % 2 == 0:
            median = (merged_arr[y-1] + merged_arr[y]) / 2.0
        
        else:
            median = merged_arr[y]
        
        return median