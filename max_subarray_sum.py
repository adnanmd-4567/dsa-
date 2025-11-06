class Solution:
    def maxSum(self, arr):
        # code here
        maximum = 0
        for i in range(len(arr)-1):
            if arr[i] + arr[i+1] > maximum:
                maximum = arr[i] + arr[i+1]

        return maximum
    