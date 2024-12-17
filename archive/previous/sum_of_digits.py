class Solution(object):
    def subtractProductAndSum(self, n):
        word = str(n)
        product=1
        sum=0
        for i in word:
            product = product * int(i)
            sum = sum + int(i)
        return product - sum
            