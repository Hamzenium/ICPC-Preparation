from collections import defaultdict
# class Solution(object):
    # def lengthOfLongestSubstring(self, s):
    #     seen = set()
    #     length = 0
    #     i = 0
    #     while i < len(s):
    #         j = i
    #         while j < len(s):
    #             if s[j] not in seen:
    #                 seen.add(s[j])
    #                 j = j + 1
    #             else:
    #                 x  =  len(seen)
    #                 length = max(x, length)
    #                 seen.clear()
    #                 j = j - 1
    #                 i = j
    #                 break
    #         i = i + 1
    #     return length


class Optimzed(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        length = 0
        i = 0
        j = 0
        
        while i < len(s) and j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
                length = max(length, j - i)
            else:
                seen.remove(s[i])
                i += 1

        return length


class BruteForce(object):
    def lengthOfLongestSubstring(self, s):
        length = 0
        
        # Try all possible substrings
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substring = s[i:j]
                
                # Check if the substring has unique characters
                if len(substring) == len(set(substring)):  # set removes duplicates
                    length = max(length, len(substring))  # Update the maximum length

        return length



s = "dvdf"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))