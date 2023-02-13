from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        count = Counter(arr)
        freq = sorted(count.values(), reverse=True)
        half = len(arr) // 2
        res = 0
        for i in freq:
            half -= i
            res += 1
            if half <= 0:
                break
        return res