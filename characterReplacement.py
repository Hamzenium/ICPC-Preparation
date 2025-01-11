from collections import defaultdict
class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        seen = set()
        counter = 0
        for i in s:
            if s not in seen:
                seen.add(s)
            else:
                counter = counter + 1







solution = Solution()
s = "ABAB"
k = 2
print(solution.characterReplacement(s,k))