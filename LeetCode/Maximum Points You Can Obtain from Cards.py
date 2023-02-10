class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = [0] * (n + 1)
        right_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            left_sum[i] = left_sum[i - 1] + cardPoints[i - 1]
        for i in range(n - 1, -1, -1):
            right_sum[i] = right_sum[i + 1] + cardPoints[i]
        res = float('-inf')
        for i in range(k + 1):
            res = max(res, left_sum[i] + right_sum[n - k + i])
        return res