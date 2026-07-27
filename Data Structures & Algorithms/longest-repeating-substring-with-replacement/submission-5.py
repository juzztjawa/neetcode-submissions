class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = {}
        n = len(s)
        for i in s:
            d[i] = d.get(i,0) + 1
        maxcount = 0
        for c in d:
            count = 0
            l = 0
            for i in range(n):
                if s[i] == c:
                    count += 1
                while (i - l +1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                maxcount = max(i -l + 1, maxcount)
                print(i,count)

        return maxcount