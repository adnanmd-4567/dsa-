class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        count = 0
        new = []
        for num in nums:
            if num != 0:
                new.append(num)
            else:
                count += 1
        nums[:] = new + ([0] * count)
