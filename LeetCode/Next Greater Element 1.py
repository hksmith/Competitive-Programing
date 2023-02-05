class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hash_map = {}
        for num in nums2:
            while stack and stack[-1] < num:
                hash_map[stack.pop()] = num
            stack.append(num)
        result = []
        for num in nums1:
            result.append(hash_map.get(num, -1))
        return result