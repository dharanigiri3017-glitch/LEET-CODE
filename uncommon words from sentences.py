class Solution:
    def uncommonFromSentences(self, s1, s2):
        words = (s1 + " " + s2).split()

        count = {}

        for word in words:
            count[word] = count.get(word, 0) + 1

        result = []

        for word in count:
            if count[word] == 1:
                result.append(word)

        return result
