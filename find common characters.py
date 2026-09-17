class Solution:
    def commonChars(self, words):
        result = list(words[0])

        for word in words[1:]:
            current = []

            for ch in result:
                if ch in word:
                    current.append(ch)
                    word = word.replace(ch, '', 1)

            result = current

        return result
