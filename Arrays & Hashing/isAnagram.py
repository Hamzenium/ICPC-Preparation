class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash1 = {}
        hash2 = {}
        if len(s) != len(t):
            return False
        
        for index in s:
            if index in hash1:
                hash1[index] += 1
            else:
                hash1[index] = 1
        for index in t:
            if index in hash2:
                hash2[index] += 1
            else:
                hash2[index] = 1
        print(hash1)
        print(hash2)
        return hash1 == hash2



solution = Solution()
input = "anagram"
output = "nagaram"

print(solution.isAnagram(input,output))