class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxlist = []
        n = len(nums)
        deque = []
        for i in range(k):
            while deque and nums[i] > nums[deque[-1]]:
                deque.pop(-1)
            deque.append(i)
        maxlist.append(nums[deque[0]])
        l = 0
        for i in range(k,n):
            if deque[0] == l:
                deque.pop(0)
            l+=1
            if len(deque) != 0:
                while deque and nums[i] > nums[deque[-1]]:
                    deque.pop(-1)
            deque.append(i)
            maxlist.append(nums[deque[0]])
        return maxlist
        