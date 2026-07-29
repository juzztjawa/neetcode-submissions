class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        set1 = set(s1)
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False
        d1 = {}
        d2 = {}
        for i in s1:
            d1[i] = d1.get(i,0) + 1
        for i in s2:
            d2[i] = d2.get(i,0) + 1
        l = 0
        d3 = {i:0 for i in d1}
        for i in range(n1):
            if s2[i] in set1:
                d3[s2[i]] = d3.get(s2[i],0) + 1
        if d3 == d1:
            return True
        for i in range(n1,n2):
            if s2[i] in set1:
                d3[s2[i]] += 1
            if s2[l] in set1:
                d3[s2[l]] -= 1
            l+=1
            if d1 == d3:
                return True
        return False