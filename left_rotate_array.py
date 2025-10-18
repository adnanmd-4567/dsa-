class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        k = k % len(nums)
        if k != 0:
            nums[:] = nums[len(nums)-k:] + nums[:-k]
        else:
            k = k % len(nums)   


        