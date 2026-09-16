class Solution:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        diff = []

        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)

        # Case 1: Exactly two positions are different
        if len(diff) == 2:
            i, j = diff
            return s[i] == goal[j] and s[j] == goal[i]

        # Case 2: Strings are already equal
        # We need at least one repeated character
        if len(diff) == 0:
            return len(set(s)) < len(s)

        return False
