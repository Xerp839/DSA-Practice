class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        local_vowels = []

        l = 0
        r = len(s) -1
        temp = 'a'

        while l < r:
            if s[l].lower in vowels:
                if s[r].lower in vowels:
                    temp = s[l]
                    s[l] = s[r]
                    s[r] = temp
                    l += 1
                    r -= 1
                r -= 1
            l += 1
        return s