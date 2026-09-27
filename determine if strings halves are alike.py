class Solution:
    def halvesAreAlike(self, s):
        vowels = "aeiouAEIOU"
        mid = len(s) // 2

        a = s[:mid]
        b = s[mid:]

        count_a = sum(ch in vowels for ch in a)
        count_b = sum(ch in vowels for ch in b)

        return count_a == count_b
