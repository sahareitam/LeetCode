class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        hashmap = {}
        res = []
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[i] > stack[-1]:
                val = stack.pop()
                hashmap[val] = nums2[i]
            stack.append(nums2[i])

        while stack:
            hashmap[stack[-1]] = -1
            stack.pop()

        for i in nums1:
            res.append(hashmap[i])

        return res

