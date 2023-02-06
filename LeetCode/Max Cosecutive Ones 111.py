class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        l = 0
        r = 0
        max_len = 0
        zero_count = 0
        while r < len(A):
            if A[r] == 0:
                zero_count += 1
            while zero_count > K:
                if A[l] == 0:
                    zero_count -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len