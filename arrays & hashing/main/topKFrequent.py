from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        # Step 1: Count frequencies of each number
        freq_dict = defaultdict(int)
        for number in nums:
            freq_dict[number] += 1
        
        # Step 2: Create a list of lists to store numbers by their frequencies
        freq_list = [[] for _ in range(len(nums) + 1)]
        for number, freq in freq_dict.items():
            freq_list[freq].append(number)
        
        # Step 3: Gather the top k frequent elements
        output = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                output.append(num)
                if len(output) == k:
                    return output



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
