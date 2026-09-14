class Solution:
    def findShortestSubArray(self, nums):
        first = {}
        count = {}
        degree = 0
        answer = len(nums)

        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i

            count[num] = count.get(num, 0) + 1
            degree = max(degree, count[num])

        for num in count:
            if count[num] == degree:
                length = nums.index(num, first[num])  # not needed
                last = max(i for i in range(first[num], len(nums)) if nums[i] == num)
                answer = min(answer, last - first[num] + 1)

        return answer
