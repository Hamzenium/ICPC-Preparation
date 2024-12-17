class Solution(object):
    def isValid(self, s):
        map = {
            "(":")",
            "{":"}",
            "[": "]"}
        stack = []
        if len(s) == 1:
            return False
        for index in range(len(s)):
            if s[index] in map.keys():
                stack.append(s[index])
            elif index not in map.keys() and stack:
                x = stack.pop()
                if map[x] != s[index]:
                    return False
            else:
                return False
        return not stack

solution = Solution()
s = ")(){}"
print(solution.isValid(s))