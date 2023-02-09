class Solution:
    def totalFruit(self, fruits):
        n, left, max_val, dict1 = len(fruits), 0, 0, collections.defaultdict(int)

        for i in range(n):
            dict1[fruits[i]] += 1

            while len(dict1) > 2:
                dict1[fruits[left]] -= 1

                if dict1[fruits[left]] == 0:
                    del dict1[fruits[left]]

                left += 1

            max_val = max(max_val,sum(dict1.values()))

        return max_val
