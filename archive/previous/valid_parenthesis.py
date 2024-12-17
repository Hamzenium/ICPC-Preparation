# class Solution(object):
#     def isValid(self,s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         dict = {
#             "(": ")",
#             "{": "}",
#             '[' : ']',
#         }
#         boolean = True
#         for char in range(len(s)):
#             if dict.get(s[char]) != None:
#                 z = s.count(s[char])
#                 w = int(char) + int(1)
#                 y = s.count(dict.get(s[char]))
#                 word = dict.get(s[char])
#                 word1 = s[w]
#                 if z != y:
#                     boolean = False
#                 # if word != word1:
#                 #     boolean = False

#         return boolean
class Solution(object):
    def isValid(self, s):
        stack = []
        Dict= {")" : "(", "]" : "[", "}" : "{"}
        for char in s:
            if char in Dict.values():
                stack.append(char)
            else:
                if stack == [] or stack.pop() != Dict[char]:
                    return False
        return stack == []
