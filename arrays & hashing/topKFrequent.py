class Solution(object):
    @staticmethod
    def topKFrequent(nums, k):
        freq_map = {}
        freq = [[] for i in range(len(nums))]
        for i in range(len(nums)):
            freq_map[nums[i]] = 1 + freq_map.get(nums[i], 0)
        for n,c in freq_map.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))  # Now works correctly
