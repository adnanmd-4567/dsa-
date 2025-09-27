class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        my_list = []
        for i in range(1,min(a,b)+1):
            if (a % i == 0 and b % i == 0):
                my_list.append(i)
        
        hcf = max(my_list)
        lcm = int((a * b)/hcf)
        
        new = [lcm,hcf]
        
        return new
            
