from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        mp = {}
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r - l + 1)
        return res
    
s = "pwwkew"
sol = Solution()
print(sol.lengthOfLongestSubstring(s))