class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        #Iniital algorithm devised :
        """1)the way on how I could solve this problem would be to first create a dicitioanry
        2)I would iterate throught the characther in that string 
        3) then I would create another dictionary for the word and count the number og 
        """
        String_table = {}
        # so first we will initilie the dictionary 

        for word in strs:
            # we will go through the each of the word in those string 
            sorted_string = ' '.join(sorted(word)) #by sorting each of the characaters in the string 
            if sorted_string not in String_table: #if the sorted string already exist then it would use exisiting one
                String_table[sorted_string] = [] # else it would create a new nested  dictioanry 
            String_table[sorted_string].append(word) # we will wehne the n append that string into the dictioanry based on that anagram 
        return String_table.values() # we will then print only the values of the dictianry to match the test cases.
    
"""
The runtime complexity of this algorithm is O(NKlog(K)), 
where N is the number of words in the strs list, and K is 
the maximum length of a word in the list. The dominant factor
in the complexity is the sorting of characters within each word, 
which takes O(Klog(K)) time, and this sorting operation is performed 
for each of the N words. So, the overall complexity is O(NK*log(K))."""

soloution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(soloution .groupAnagrams(strs))


    
            
        