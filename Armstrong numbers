class Solution:
    def armstrongNumber (self, n):
        # code here
        result = 0
        remaining_number = n
        int_list = []
        
        while remaining_number > 0:
            last_digit = remaining_number % 10
            remaining_number = remaining_number//10
            int_list.append(last_digit)
        
        for i in int_list:
            result += (i ** 3)
            
        if result == n:
            return True
        else:
            return False
