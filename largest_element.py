class Solution:
    def largest(self, arr):
        # code here
        temp = arr[0]
        for i in range(len(arr)):
            if arr[i] > temp:
                temp = arr[i]
        return temp