
class Solution:
    def distributeCandies(self, candyType):
        n = len(candyType)

        different_types = len(set(candyType))

        return min(different_types, n //2)
