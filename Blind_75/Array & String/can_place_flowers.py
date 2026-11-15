class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
    
        for i in  range(len(flowerbed)):

            if n <= 0:
                return True

            if flowerbed[i] == 1:
                continue

            left_empty = (i == 0 or flowerbed[i-1] == 0)
            right_empty = (i == len(flowerbed)-1 or flowerbed[i+1] == 0)

            if left_empty and right_empty:
                flowerbed[i] = 1
                n -= 1

        return True if n <= 0 else False