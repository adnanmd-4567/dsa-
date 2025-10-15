class Solution:
    def isPalindrome(self, x: int) -> bool:
        remaining_number = x
        reversed_number = 0
        if x < 0:
            return False
        while remaining_number > 0:
            last_digit = remaining_number % 10
            remaining_number = remaining_number // 10
            reversed_number = (reversed_number * 10) + last_digit
        if x == reversed_number:
            return True
        else:
            return False
            
