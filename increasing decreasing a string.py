class Solution:
    def sortString(self, s):
        result = ""
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        while len(result) < len(s):
            for i in range(26):
                if freq[i] > 0:
                    result += chr(i + ord('a'))
                    freq[i] -= 1

            for i in range(25, -1, -1):
                if freq[i] > 0:
                    result += chr(i + ord('a'))
                    freq[i] -= 1

        return result
