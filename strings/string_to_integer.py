class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        num = 0
        
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            
            if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN
            
            num = num * 10 + digit
            i += 1
        
        return sign * num
        