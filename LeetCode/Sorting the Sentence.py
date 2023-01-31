class Solution:
    def sortSentence(self, s: str) -> str:
        sort = s.split(" ")
        final_ans = ""

        for i in range (len(sort)):
            min_index = i
            for j in range (i + 1, len(sort)):
                if sort[j][-1] < sort[min_index][-1]:
                    min_index = j
            if i != min_index:
                sort[min_index], sort[i] = sort[i], sort[min_index]
            final_ans += sort[i][:-1] + ' '
        return (final_ans[:-1])