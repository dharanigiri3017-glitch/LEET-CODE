class Solution:
    def maxRepeating(self, sequence, word):
        count = 0
        repeated = word

        while repeated in sequence:
            count += 1
            repeated += word

        return count
