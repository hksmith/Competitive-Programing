from typing import List

class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        def flip(sublist, k):
            i = 0
            j = k - 1
            while i < j:
                sublist[i], sublist[j] = sublist[j], sublist[i]
                i += 1
                j -= 1
        
        res = []
        for i in range(len(A), 1, -1):
            max_idx = A.index(max(A[:i]))
            if max_idx != i - 1:
                if max_idx != 0:
                    res.append(max_idx + 1)
                    flip(A, max_idx + 1)
                res.append(i)
                flip(A, i)
        return res