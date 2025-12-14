class Solution:
    def countSubstr (self, s, k):
        # Code here
        from collections import defaultdict
        
        def atMostK(k):
            left = 0
            freq = defaultdict(int)
            count = 0
            
            for right in range(len(s)):
                freq[s[right]] += 1
                
                while len(freq) > k:
                    freq[s[left]] -= 1
                    if freq[s[left]] == 0:
                        del freq[s[left]]
                    left += 1
                
                count += right - left + 1
            
            return count
        
        return atMostK(k) - atMostK(k - 1)