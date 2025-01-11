
class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()
        counter = 1  # Start with one partition by default
        for char in s:
            if char in seen:
                counter += 1  # If duplicate found, increment the partition count
                seen.clear()  # Reset the set for the new partition
            seen.add(char)  # Add current character to the set
        return counter

class BruteForce(object):
   def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        seen = set()
        counter = 0
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] not in seen:
                    seen.add(s[j])
                    j = j + 1
                else:
                    counter = counter + 1
                    seen.clear()
                    break
            i = j
            i = i + 1
        if len(seen) > 0:
            counter = counter + 1
        return counter

s = "cuieokbs"
sol = Solution()
print(sol.partitionString(s))