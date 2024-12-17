class bubblesort(object):

    def sort(self,s):
        n = len(s)
        for i in range(n):
            for j in range(0, n - i - 1):
                if s[j] > s[j + 1]:
                    s[j], s[j+1] = s[j+1], s[j]
        return s

arr = [64, 34, 25, 12, 22, 11, 90]
# in this algorithm we use the bubble sorting algorithm which runs in O(n^2), 
#it compares the first index with one index ahead of it and switches if the value is more j+1 is more than it .

algorithm = bubblesort()
print(algorithm.sort(arr))