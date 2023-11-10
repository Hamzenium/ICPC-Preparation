class Solution(object):
    def firstUniqChar(self, s):
        dict= {}
        for i in s:
            if(dict.get(i)== None):
                dict[i]= 1
            else: dict[i]+=1
        for i in range(len(s)):
            if(dict[s[i]]== 1):
                return i
        return -1
