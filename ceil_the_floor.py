class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        floor = -1
        ceil = -1
        
        for num in arr:
            if num <= x and num > floor:
                floor = num
                
            if num >= x and (ceil == -1 or num < ceil):
                ceil = num
                
        return floor,ceil