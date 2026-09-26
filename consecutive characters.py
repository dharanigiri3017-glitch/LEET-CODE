class Solution:
    def maxPower(self, s):
        count = 1
        max_count = 1

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                count = 1

            max_count = max(max_count, count)

        return max_count
