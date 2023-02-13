class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            heap.append((dist, p))
        
        heap = heapq.nsmallest(K, heap)
        return [p[1] for p in heap]