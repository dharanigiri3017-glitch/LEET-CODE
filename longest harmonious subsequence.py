
class Solution:
    def findLHS(self, nums):
        count = {}

        # Count each number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        ans = 0

        # Check consecutive values
        for num in count:
            if num + 1 in count:
                ans = max(ans, count[num] + count[num + 1])

        return ans

