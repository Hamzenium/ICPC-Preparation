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
class bruteforce(object):
    @staticmethod
    def topKFrequent(nums, k):
        # Count frequency of each element
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        # Sort elements by frequency in descending order using lambda
        sorted_nums = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the top k frequent elements
        res = []
        for i in range(k):
            res.append(sorted_nums[i][0])
        
        return res

nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution()
print(sol.topKFrequent(nums, k))  # Now works correctly
