class Solution:
    def thousandSeparator(self, n):
        s = str(n)
        result = ""

        for i in range(len(s)):
            result += s[i]

            if (len(s) - i - 1) % 3 == 0 and i != len(s) - 1:
                result += "."

        return result
