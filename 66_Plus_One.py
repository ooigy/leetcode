class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
       # idea: add to last digit, if 9, carry over
        if not digits: return [1]
        digits[-1] += 1
        if digits[-1] < 10:
            return digits
        else:
            return self.plusOne(digits[:-1]) + [0]