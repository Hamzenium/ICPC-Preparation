nums = [1,5,3,4,6]
profit = [2,13,4,5,6]
print(nums.sort())
vector = set()
def function(nums, profit):
    length = len(nums)
    sum = 0
    for days in range(len(nums)):
        if (days + 2) <= length-1 and (days - 2 >=0):
            foward = profit[days] + profit[days+1] + profit[days+2]
            back = profit[days] + profit[days-1] + profit[days-2]
            if(foward > back and foward > sum):
                sum = foward
            elif(back > foward and back > sum):
                sum =  back
        elif days + 2 <= length-1:
            result = profit[days] + profit[days+1] + profit[days+2]
            if result > sum:
                sum = result
        elif days - 2 >= 0:
             result = profit[days] + profit[days-1] + profit[days-2]
             if result > sum:
                sum = result
    return sum

print(function(nums,profit))

array1 = [4, 1, 3, 2]
array2 = [3, 4, 5, 6]

# Create a list of pairs
pairs = [(x, y) for x, y in zip(array2, array1)]

# Sort the list based on array1
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])

# Create a set from the sorted list of pairs
result_set = set(sorted_pairs)

print(result_set)
