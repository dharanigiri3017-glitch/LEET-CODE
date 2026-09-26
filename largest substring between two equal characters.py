class Solution:
    def maxLengthBetweenEqualCharacters(self, s):
        max_len = -1

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    max_len = max(max_len, j - i - 1)

        return max_len
