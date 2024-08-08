class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        temp = abs(x)

        while temp > 0:
            rem = temp % 10
            rev = rev * 10 + rem
            temp //= 10

        if x < 0:
            rev = -rev

        if x < -2**31 or x > 2**31 -1:
             return 0

        return rev
