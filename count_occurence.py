class Solution:
    def countFreq(self, arr, target):
        # code here
        def firstSearch(arr,target):
            left = 0
            right = len(arr) - 1
            first = -1
            while left <= right:
                mid = (left + right) // 2 
                
                if arr[mid] == target:
                    first = mid
                    right = mid - 1
                    
                elif arr[mid] < target:
                    left = mid + 1
                    
                else:
                    right = mid - 1
                    
            return first
            
        def lastSearch(arr,target):
            left = 0
            right = len(arr) - 1
            last = -1
            while left <= right:
                mid = (left + right) // 2 
                
                if arr[mid] == target:
                    last = mid
                    left = mid + 1
                    
                elif arr[mid] < target:
                    left = mid + 1
                    
                else:
                    right = mid - 1
                    
            return last
                 
        first = firstSearch(arr, target)
        last = lastSearch(arr, target)
        if first == -1:
            return 0
        return (last - first) + 1
                
            
        