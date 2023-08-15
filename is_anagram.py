class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        s1 = {}
        t1 = {}
        for char in s:
            if char in s1:
                s1[char] += 1
            else:
                s1[char] = 1
        for char in t:
            if char in t1:
                t1[char] += 1
            else:
                t1[char] = 1
        return s1 == t1
    
# in this problem we have solved the problem with O(n)
#if the length of the both the strings do not have the same length it gives false
# else it interates through each of the string and adds it into the s1 dictionary, if it finds that char again it adds it number
#it iterates through both of the strings in the same manner
# it then checks both of the string and gives either false or true
solution = Solution()
print(solution.isAnagram("listen", "silent"))  # Output: True
print(solution.isAnagram("hello", "world"))    # Output: False






            
