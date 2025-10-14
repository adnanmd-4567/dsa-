class Solution:
    def largest(self, arr):
        temp = arr[0]
        new = []
        for i in range(len(arr)):
            if arr[i] > temp:
                temp = arr[i]
            else:
                new.append(arr[i])
        
        temp2 = new[0]
    
        if len(new) == 0:
            return -1
        
        else:
            for i in range(len(new)):
                if new[i] > temp2:
                    temp2 = new[i]
            return temp2
