class Solution: 
    def selectionSort(self, arr):
        #code here
        for i in range(len(arr)):
            for j in range(len(arr) -1):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        return arr
