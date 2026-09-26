class Solution:
    def restoreString(self, s, indices):
        result = [""] * len(s)

        for i in range(len(s)):
            result[indices[i]] = s[i]

        return "".join(result)
