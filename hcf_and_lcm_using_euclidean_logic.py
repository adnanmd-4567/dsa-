class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        # code here
        x,y = a,b
        while y:
            x,y = y, (x % y)
  
        hcf = x
        lcm = int((a * b)/hcf)
        new = [lcm,hcf]
        
        return new
