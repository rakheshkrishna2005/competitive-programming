class Solution:
    def isPalindrome(self, x: int) -> bool:
        sum = 0
        temp = x
        while temp>0:
            digit = temp % 10
            sum = sum * 10 + digit
            temp //= 10
        if x == sum:
            return True
        else:
            return False
