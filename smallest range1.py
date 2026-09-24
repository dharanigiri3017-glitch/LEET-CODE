class Solution:
    def smallestRangeI(self, nums, k):
        minimum = min(nums)
        maximum = max(nums)

        score = (maximum - k) - (minimum + k)

        return max(0, score)
