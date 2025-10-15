class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        while x!= 0:

            last_digit = x % 10
            x = x // 10
            
            if result > (2**31 - 1) // 10 or (result == (2**31 - 1) // 10 and last_digit > 7):
                return 0
        
            result = result * 10 + last_digit
        return (sign * result)
        
