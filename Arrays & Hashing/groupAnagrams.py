class Solution(object):
    def groupAnagrams(self, strs):
        dic = {}
        for string in strs:
            current = sorted(string)
            current = "".join(current)
            if current in dic:
                dic[current].append(string)
                
            else:
                dic[current] = [string]
                
        ans = []
        for string in dic:
            ans.append(dic[string])
            
        return ans
solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))