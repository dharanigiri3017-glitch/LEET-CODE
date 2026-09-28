class Solution:
    def longestNiceSubstring(self,s):
        if len(s) < 2:
            return ""

        for i in range(len(s)):
            if s[i].lower() not in s or s[i].upper() not in s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                return left if len(left) >= len(right) else right

        return s
