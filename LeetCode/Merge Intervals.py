class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            curr_intv = intervals[i]
            previous_interval = result[-1]
            if curr_intv[0] <= previous_interval[1]:
                result[-1][1] = max(curr_intv[1], previous_interval[1])
            else:
                result.append(curr_intv)
        return result