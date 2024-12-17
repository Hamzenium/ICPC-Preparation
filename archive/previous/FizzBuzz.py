class Solution(object):
    def fizzBuzz(self, n):
        array = []
        i = 1
        while i < n+1:
            if i % 3 == 0 and i % 5 == 0:
                array.append("FizzBuzz")
            elif i % 3 == 0:
                array.append("Fizz")
            elif i % 5 == 0:
                array.append("Buzz")
            else:
                array.append(str(i))
            i = i + 1
        return array
