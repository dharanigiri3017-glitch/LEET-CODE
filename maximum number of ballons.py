class Solution:
    def maxNumberOfBalloons(self, text):
        count = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }

        for ch in text:
            if ch in count:
                count[ch] += 1

        count['l'] //= 2
        count['o'] //= 2

        return min(count.values())
