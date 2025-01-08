class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        actions = 0
        for i in count:
            if (k - i) in count:
                if i == (k - i):
                    while count[i] >= 2:
                        count[i] -= 2
                        actions += 1
                elif count[i] >= 1 and count[k-i] >= 1:
                    while count[i] >= 1 and count[k-i] >= 1:
                        count[i] -= 1
                        count[k-i] -= 1
                        actions +=1
        return actions

