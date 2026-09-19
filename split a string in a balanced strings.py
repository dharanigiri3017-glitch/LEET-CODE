class Solution:
    def balancedStringSplit(self, s):
        count = 0
        answer = 0

        for ch in s:
            if ch == 'L':
                count += 1
            else:
                count -= 1

            if count == 0:
                answer += 1

        return answer
