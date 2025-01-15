class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_val = arr[n - 1]
        temp = arr[n - 1]
        for i in range(1, len(arr)):
            if arr[n - 1 - i] > max_val:
                temp = arr[n - 1 - i]
            arr[n - 1 - i] = max_val
            max_val = temp
        arr[n - 1] = -1
        return arr
