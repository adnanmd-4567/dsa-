class Solution:
 
    def mergeSort(self, arr, l, r):
        #code here
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)

    def merge(self, arr, l, mid, r):
        temp1 = mid - l + 1
        temp2 = r - mid

        L = arr[l : mid + 1]
        R = arr[mid + 1 : r + 1]

        i = j = 0
        k = l

        while i < temp1 and j < temp2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < temp1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < temp2:
            arr[k] = R[j]
            j += 1
            k += 1
