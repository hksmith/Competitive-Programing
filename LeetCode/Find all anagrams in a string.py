class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ls, lp = len(s), len(p)
        if ls<lp: return
        anagrams, cs, cp = [], Counter(s[:lp]), Counter(p)
        if cs==cp: anagrams.append(0)
        for i in range(ls-lp):
            prev, curr = s[i], s[i+lp] ## current window s[i+1:i+lp]
            cs[prev] -= 1
            if cs[prev]==0:
                del cs[prev]
            cs[curr] += 1
            if cs==cp:
                anagrams.append(i+1)
        return anagrams