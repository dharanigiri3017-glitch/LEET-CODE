class Solution:
    def reformat(self, s):
        letters = []
        digits = []

        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                digits.append(ch)

        if abs(len(letters) - len(digits)) > 1:
            return ""

        result = []

        if len(letters) > len(digits):
            first = letters
            second = digits
        else:
            first = digits
            second = letters

        for i in range(len(second)):
            result.append(first[i])
            result.append(second[i])

        if len(first) > len(second):
            result.append(first[-1])

        return "".join(result)
