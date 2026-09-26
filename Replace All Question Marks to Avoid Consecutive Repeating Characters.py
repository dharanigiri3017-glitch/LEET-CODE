class Solution:
    def modifyString(self, s):
        s = list(s)

        for i in range(len(s)):
            if s[i] == '?':
                for ch in 'abc':
                    if (i == 0 or s[i - 1] != ch) and (i == len(s) - 1 or s[i + 1] != ch):
                        s[i] = ch
                        break

        return "".join(s)
