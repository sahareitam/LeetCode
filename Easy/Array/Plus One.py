class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = -1
        while digits[d] == 9:
            digits[d] = 0
            d -= 1
            if abs(d) > len(digits):
                digits = [0] + digits
                break
        digits[d] += 1
        return digits
