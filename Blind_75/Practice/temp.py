class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        result = []
        max = candies[0]

        for i in range(len(candies)):
            if candies[i] > max:
                max = candies[i]

        for i in range(len(candies)):
            if candies[i] + extraCandies > max:
                result.append(True)
            else:
                result.append(False)
        return result