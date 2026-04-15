class Solution:
    def reverse(self, x: int) -> int:
        # handle negatives
        is_negative = False
        if x < 0:
            x = x * -1
            is_negative = True

        # build reversed int make sure we are not overflowing
        result = 0
        while x:
            remainder = x % 10
            x = x // 10  # integer division
            result = result * 10 + remainder

        # check overflow limit
        MAX_INT = 2147483647
        if result > MAX_INT:
            return 0
        return result * -1 if is_negative else result
