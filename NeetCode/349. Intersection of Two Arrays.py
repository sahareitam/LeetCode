class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        if len(nums1) > len(nums2):
            Sl = set(nums1)
            Ss = set(nums2)
        else:
            Ss = set(nums1)
            Sl = set(nums2)
        for i in Ss:
            if i in Sl:
                res.append(i)
        return res