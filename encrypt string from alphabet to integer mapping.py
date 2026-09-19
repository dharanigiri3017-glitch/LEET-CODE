class Solution:
    def freqAlphabets(self, s):
        result = ""
        i = 0

        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                num = int(s[i:i+2])
                result += chr(96 + num)
                i += 3
            else:
                num = int(s[i])
                result += chr(96 + num)
                i += 1

        return result
