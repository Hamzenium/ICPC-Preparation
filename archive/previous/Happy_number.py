class Solution:
    def isHappy(self, n: int) -> bool:
        word = str(n)
        counter = 0
        sum = 0
        while (word != "1"):
            for i in word:
                sum += int(i) * int(i)
            counter = counter + 1
            if counter == 50:
                return False
            word = str(sum)
            sum = 0
        return True






