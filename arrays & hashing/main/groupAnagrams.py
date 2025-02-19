class Solution(object):
    def groupAnagrams(self,strs):
        result = []
        i = 0
        for word in strs:
            letter = strs.pop(0)
            anagrams = [letter]
            while i < len(strs):
                if sorted(letter) == strs[i]:
                    anagrams.append(strs.pop(i))
                else:
                    i = i + 1
            result.append(anagrams)
        return result




class Optimzed(object):
    def groupAnagrams(self, strs):
        anagrams_dict = {}
        for word in strs:
            # Sort the word to find the anagram key
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagrams_dict:
                anagrams_dict[sorted_word].append(word)  # Append the word to the existing list
            else:
                anagrams_dict[sorted_word] = [word]  # Create a new list for this sorted word
        return list(anagrams_dict.values())  # Return only the grouped anagrams as a list of lists

strs = ["eat","tea","tan","ate","nat","bat"]
solution = Solution()
print(solution.groupAnagrams(strs))