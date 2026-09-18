class Solution:
    def findOcurrences(self, text, first, second):
        words = text.split()
        result = []

        for i in range(len(words) - 2):
            if words[i] == first and words[i + 1] == second:
                result.append(words[i + 2])

        return result
