class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []

        def rec(i, sub, total):
            if total > target or i >= len(candidates):
                return
            if total == target:
                self.res.append(sub)
                return
            rec(i, sub + [candidates[i]], total + candidates[i])
            for j in range(i + 1, len(candidates)):
                rec(j, sub + [candidates[j]], total + candidates[j])

        rec(0, [], 0)
        return self.res