class Solution(object):
    def generate(self, numRows):
        result = []
        if numRows == 0:
            return []
        for row in range(numRows):
            newrow = [0 for _ in range(row + 1)]
            newrow[0], newrow[-1] = 1 , 1
            for i in range(1,len(newrow) - 1):
                newrow[i] = result[-1][i] + result[-1][i-1]
            result.append(newrow)
        return result
        
        
