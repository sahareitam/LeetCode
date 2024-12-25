class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 0
        k = 0
        for i in range(len(nums)):
            cur_num_to_count = nums[counter]
            while cur_num_to_count == nums[counter]:
                counter += 1
                if counter == len(nums):
                    break
            nums[i] = cur_num_to_count
            if counter == len(nums):
                k = i + 1
                break
        return k

