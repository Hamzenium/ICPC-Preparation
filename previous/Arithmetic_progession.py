class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort(reverse=True)
        difference = arr[0] - arr[1]
        boolean = True
        for i in range(len(arr)):
            if (i + 1 < len(arr)) and (arr[i] - arr[i + 1] != difference):
                boolean = False
        return boolean

