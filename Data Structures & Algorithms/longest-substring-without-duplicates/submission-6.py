class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n ==0:
            return 0
        uniquechar = set()
        l = 0
        maxcount = 0
        count = 0
        for i in range(n):
            if s[i] in uniquechar:
                while s[i]!=s[l]:
                    uniquechar.remove(s[l])
                    l+=1
                    count -=1
                uniquechar.remove(s[l])
                l+=1
                count -=1
            uniquechar.add(s[i])
            count+=1
            maxcount = max(count,maxcount)
            
        return maxcount