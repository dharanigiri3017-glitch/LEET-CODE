class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split()

        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i + 1

        return -1
