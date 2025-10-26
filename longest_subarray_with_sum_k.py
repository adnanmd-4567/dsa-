class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        prefix_sum = 0
        seen = {}
        max_len = 0
        
        for i in range(len(arr)):
            prefix_sum += arr[i]
            
            if prefix_sum == k:
                max_len = i + 1
                
            if (prefix_sum - k) in seen:
                length = i - seen[prefix_sum - k]
                if length > max_len:
                    max_len = length
                    
            if prefix_sum not in seen:
                seen[prefix_sum] = i
                
        return max_len