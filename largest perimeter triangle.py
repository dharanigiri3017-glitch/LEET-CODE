class Solution:
    def largestPerimeter(self, nums):
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            a = nums[i - 2]
            b = nums[i - 1]
            c = nums[i]

            if a + b > c:
                return a + b + c

        return 0
