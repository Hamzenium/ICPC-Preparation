class Solution(object):
    def lengthOfLongestSubstring1(self, s):

        seen = {}
        l = 0
        output = 0
        for r in range(len(s)):
            if s[r] not in seen:
                output = max(output,r-l+1)
            else:
                if seen[s[r]] < l:
                    output = max(output,r-l+1)
                else:
                    l = seen[s[r]] + 1
            seen[s[r]] = r
        return output

solution = Solution()
strs = "abcabcbb"
print(solution.lengthOfLongestSubstring1(strs))

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict = {}
        output = ""
        word = ""
        if len(s) == 1:
            return 1
        elif len(s) == 2 and s[0] != s[1]:
            return 2
        elif len(s) == 2 and s[0] == s[1]:
            return 1
        else:
            for i in range(len(s)):
                if s[i] not in dict:
                    word += s[i]
                    dict[s[i]] = 1
                else:
                    if len(word) > len(output):
                        output = word
                    if i > 2:
                        word = ""
                        word += s[i-1]
                    word += s[i]
                    dict = {}
                    dict [s[i]] = 1
                    dict [s[i-1]] = 1
        if len(word) > len(output):
            output = word
        return len(output)

# 135 pm