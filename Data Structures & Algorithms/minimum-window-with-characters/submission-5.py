class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        if n2 > n1:
            return ''
        d2 = {}
        for i in t:
            d2[i] = d2.get(i,0) + 1
        have = len(d2)
        need = 0
        l = 0
        minsubstr = []
        minlength = float('inf')
        d3 = {i:0 for i in d2}
        for i in range(n1):
            if s[i] in d3:
                d3[s[i]] += 1
                if d3[s[i]] == d2[s[i]]:
                    need +=1
            while have == need:
                if (i-l+1) < minlength:
                    minlength = i-l+1
                    minsubstr = [l,i+1]
                if s[l] in d3:
                    d3[s[l]] -= 1
                    if d3[s[l]] < d2[s[l]]:
                        need -=1
                l += 1
        if minsubstr == []:
            return ''
        return s[minsubstr[0]:minsubstr[1]]