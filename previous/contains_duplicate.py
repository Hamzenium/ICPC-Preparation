
def containsDuplicate(self, nums):

    seen = set()
    for number in nums:
        if number in seen:
            return True
        seen.add(number)
    return False

# in this code the time complexity of this algorithm is o(n)
# for number in nums it  would be 0(n), since it iterates through all the array
# if number in nums would be o(1), since we are using set which stores a unique number
# if it finds the  number it gives true, else adds the number
# Sets can only contain unique elements. If you try to add a duplicate element, it won't be stored multiple times. 