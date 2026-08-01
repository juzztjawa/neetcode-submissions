class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        maxlist = []
        n = len(nums)
        deq = deque()
        for i in range(k):
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()
            deq.append(i)
        maxlist.append(nums[deq[0]])
        l = 0
        for i in range(k,n):
            if deq[0] == l:
                deq.popleft()
            l+=1
            if len(deq) != 0:
                while deq and nums[i] > nums[deq[-1]]:
                    deq.pop()
            deq.append(i)
            maxlist.append(nums[deq[0]])
        return maxlist
        