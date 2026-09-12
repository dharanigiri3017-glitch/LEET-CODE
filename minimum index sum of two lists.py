
class Solution:
    def findRestaurant(self, list1, list2):
        # Store index of each string in list1
        index_map = {}

        for i in range(len(list1)):
            index_map[list1[i]] = i

        min_sum = float('inf')
        result = []

        # Check common strings
        for j in range(len(list2)):
            if list2[j] in index_map:
                index_sum = index_map[list2[j]] + j

                if index_sum < min_sum:
                    min_sum = index_sum
                    result = [list2[j]]

                elif index_sum == min_sum:
                    result.append(list2[j])

        return result

