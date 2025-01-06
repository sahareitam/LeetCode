class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        intersec = set(nums1) & set(nums2)
        print(intersec)
        return [list(set(nums1) - intersec), list(set(nums2) - intersec)]

