class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        # Initialize a table to store whether substrings are palindromes
        dp = [[False] * n for _ in range(n)]

        start = 0  # Variable to track the starting index of the longest palindrome
        max_len = 1  # Variable to track the length of the longest palindrome

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check substrings of length 3 and greater
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                # Check if the substring is a palindrome
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    start = i
                    max_len = length

        # Return the longest palindromic substring
        return s[start:start + max_len]



n = "babad"
algorithm = Solution()
print(algorithm.longestPalindrome(n))