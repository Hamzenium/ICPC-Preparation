class Solution(object):
    def merge(nums1, m, nums2, n):
        list = [0 for i in range(m + n)]
        counter = 0
        nums1.sort(reverse = True)
        nums2.sort(reverse=True)

        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                list[counter] = nums1[m]
                counter = counter + 1
                m = m - 1
            elif nums1[m-1] > nums2[n-1]:
                list[counter] = nums2[n-1]
                counter = counter + 1
                n = n - 1
            else:
                list[counter] = nums1[m-1]
                counter = counter + 1
                list[counter] = nums2[n-1]
                n = n - 1
                m = m - 1
        return list

    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print(merge(nums1,m,nums2,n))
