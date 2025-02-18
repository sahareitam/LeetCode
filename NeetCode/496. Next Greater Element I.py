class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # n = len(nums2)
        # for i,num in enumerate(nums1):
        #     checker =nums2.index(num)
        #     while checker < n-1 and num >= nums2[checker]:
        #         checker += 1
        #     if nums2[checker] > num:
        #         nums1[i] = nums2[checker]
        #     else:
        #         nums1[i] = -1
        # return nums1
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

