class Solution:
    def findRelativeRanks(self, score):
        sorted_score = sorted(score, reverse=True)

        rank = {}

        for i, value in enumerate(sorted_score):
            position = i + 1

            if position == 1:
                rank[value] = "Gold Medal"
            elif position == 2:
                rank[value] = "Silver Medal"
            elif position == 3:
                rank[value] = "Bronze Medal"
            else:
                rank[value] = str(position)

        return [rank[value] for value in score]
