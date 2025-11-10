class Solution:
    def leaders(self, arr):
        # code here
        new = reversed(arr)
        maximum = 0
        result = []
        for i in reversed(arr):
            if i >= maximum:
                maximum = i
                result.append(maximum)
        new_result = reversed(result)
        return new_result
            