#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        return
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(len(arr)):
            m = i
            
            for j in range(i + 1, len(arr)):
                if arr[m] > arr[j]:
                    m = j
            arr[i], arr[m] = arr[m], arr[i]