#!/usr/bin/env python3


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        len1 = len(nums1)
        len2 = len(nums2)
        i = 0
        j = 0

        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < len1:
            res.append(nums1[i])
            i += 1

        while j < len2:
            res.append(nums2[j])
            j += 1

        if len(res) % 2 == 0:
            med = int(len(res) / 2)
            return (res[med] + res[med - 1]) / 2.0
        else:
            med = int(len(res) / 2)
            return res[med]


if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2]
    nums2 = [3, 4]
    result = s.findMedianSortedArrays(nums1, nums2)
    print(result)
