class Solution:
    def countCharacters(self,words, chars) :
        total = 0

        for word in words:
            temp = list(chars)
            possible = True

            for ch in word:
                if ch in temp:
                    temp.remove(ch)
                else:
                    possible = False
                    break

            if possible:
                total += len(word)

        return total
