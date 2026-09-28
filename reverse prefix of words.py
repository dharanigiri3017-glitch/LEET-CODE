class Solution:
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word

        i = word.index(ch)

        return word[:i+1][::-1] + word[i+1:]
