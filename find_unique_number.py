class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        new = sorted(nums)
        count = 0
        my_list = []
        n = len(new)
        if n == 1:
            return new[0]
        else:
            for i in range(len(new)-1):
                if new[i] == new[i + 1]:
                    count += 1
                    if count == 1:
                        my_list.extend([new[i],new[i]])
                        count = 0
            diff = set(new) - set(my_list)
            return diff.pop()