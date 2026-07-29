class Solution(object):
    def longestPalindrome(self, s):
        
        count = Counter(s)
        ans = 0

        for freq in count.values():
            ans += (freq // 2) * 2

        if ans < len(s):
            ans += 1

        return ans
