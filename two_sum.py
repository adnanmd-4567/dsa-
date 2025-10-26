class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_dict = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in my_dict:
                return [my_dict[diff],i]
            my_dict[num] = i