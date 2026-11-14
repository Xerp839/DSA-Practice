class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        local_vowels = []
        s = list(s)
        l = 0
        r = len(s) -1
        temp = 'a'

        while l < r:

            if s[l].lower() not in vowels:
                l += 1

            elif s[r].lower() not in vowels:
                r -= 1

            else:
                s[l], s[r] = s[r] , s[l]
                l += 1
                r -= 1
        return "".join(s)