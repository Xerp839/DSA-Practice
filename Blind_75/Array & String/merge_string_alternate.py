class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l = 0
        r = 0

        switch = 0
        merged = []

        while l < len(word1) and r < len(word2):
            if switch == 0:
                merged.append(word1[l])
                l += 1
                switch = 1
            else:
                merged.append(word2[r])
                r += 1
                switch = 0
        
        while l < len(word1):
            merged.append(word1[l])
            l += 1
        
        while r < len(word2):
            merged.append(word2[r])
            r += 1

        return "".join(merged)