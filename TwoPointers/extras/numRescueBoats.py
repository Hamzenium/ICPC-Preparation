class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people = sorted(people)
        l,r = 0 , len(people) - 1
        boats = 0
        while l <= r:
            if people[l] + people[r] <= limit:
                l = l + 1
            r = r - 1
            boats += 1
        return boats
