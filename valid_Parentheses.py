
class Solution(object):
    def isValid(self, s):
        stack = []
        dict = {
            "(": ")",
            "{": "}",
            '[' : ']'
            }
        for i in s:
            if i in dict.keys():
                stack.append(i)
            else:
                if stack == [] or dict[stack.pop()] != i:
                    return False
        return True
    
algorithm = Solution()
s = "()[]{}"
print(algorithm.isValid(s))