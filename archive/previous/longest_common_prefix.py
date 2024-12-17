class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        counter = 0
        boolean = True
        string = ""
        pre_string = ""
        result = []
        for word in range(len(strs)+2):

            if word < len(strs) - 2:
                if strs[word] == "":
                    return ""
                if len(strs[word]) == 1 and len(strs)==1:
                    return strs[0]


            for letter in range(len(strs)):
                if len(strs[letter])-1 < counter:
                    return "".join(result)   
                string = strs[letter][counter]
                if string != pre_string and pre_string != "":
                    boolean = False
                pre_string = strs[letter][counter]

            if boolean == True:
                result.append(strs[letter][counter])
            if boolean == False:
                return "".join(result)   
            boolean = True
            counter = counter + 1
            pre_string = ""
        return "".join(result)



    

                
