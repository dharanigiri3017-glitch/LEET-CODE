class Solution:
    def sortSentence(self, s) :
        words = s.split()
        result = [""] * len(words)

        for word in words:
            pos = int(word[-1]) - 1
            result[pos] = word[:-1]

        return " ".join(result)
