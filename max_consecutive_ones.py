class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        my_list = []
        count = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                my_list.append(count)
                count = 0
                
        my_list.append(count)
        return max(my_list)
