class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        word = ""
        for i in s:
            if i not in word:
                word += s
            else:
                dict.add(word)
                word = ""
        dict
            
solution = Solution()
s = "abcabcbb"
print(solution.lengthOfLongestSubstring(s))