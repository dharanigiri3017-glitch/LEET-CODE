class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        duplicate = 0
        missing = 0

        for i in range(1, n + 1):
            count = nums.count(i)

            if count == 2:
                duplicate = i
            elif count == 0:
                missing = i

        return [duplicate, missing]
