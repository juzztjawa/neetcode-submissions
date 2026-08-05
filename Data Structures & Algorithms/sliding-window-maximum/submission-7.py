class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        que = deque()
        n = len(nums)
        finalres = []
        l = 0
        for i in range(n):
            while que and nums[que[-1]] <= nums[i]:
                que.pop()
            que.append(i)
            if l > que[0]:
                que.popleft()
            if i + 1>= k:
                finalres.append(nums[que[0]])
                l+=1



        return finalres
