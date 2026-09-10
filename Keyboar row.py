class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = set(word.lower())

            if w <= row1 or w <= row2 or w <= row3:
                result.append(word)

        return result
