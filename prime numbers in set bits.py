class Solution:
    def countPrimeSetBits(self, left, right):
        count = 0

        for num in range(left, right + 1):
            bits = bin(num).count("1")

            if bits in [2, 3, 5, 7, 11, 13, 17, 19]:
                count += 1

        return count
