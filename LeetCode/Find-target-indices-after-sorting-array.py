class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        a = []
        j = 0
        for i in nums:
            if i == target:
                a.append(j)
            j += 1
        return a