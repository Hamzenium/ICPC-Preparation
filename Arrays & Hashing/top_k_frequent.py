class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        seen = {}
        results = []
        for index in nums:
            i =int(index)
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        sortedNums = sorted(seen.items(), key=lambda x: x[1], reverse=True)
        for idx in range(0, k):
            results.append(sortedNums[idx][0])
        return results  