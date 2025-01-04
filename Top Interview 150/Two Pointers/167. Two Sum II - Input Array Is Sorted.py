class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(numbers)):
            com = target-numbers[i]
            if com in dic:
                return [dic[com],i+1]
            dic[numbers[i]] = i + 1