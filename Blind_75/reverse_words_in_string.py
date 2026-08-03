class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split()
        reversed = ""
        for i in s:
            reversed = i +" "+ reversed
        
        return reversed