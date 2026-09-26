class Solution:
    def maxScore(self, s):
        zeros = 0
        ones = s.count('1')
        max_score = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            score = zeros + ones
            max_score = max(max_score, score)

        return max_score
