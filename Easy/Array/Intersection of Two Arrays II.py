class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        res = []
        if len(nums1) > len(nums2):
            s = nums2
            b = nums1
        else:
            s = nums1
            b = nums2

        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for j in b:
            if j in hashmap and hashmap[j] > 0:
                hashmap[j] -= 1
                res.append(j)

        return res
