class Solution:
    def removePalindromeSub(self,s):
        if s == s[::-1]:
            return 1
        return 2
