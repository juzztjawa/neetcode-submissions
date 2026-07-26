class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longlength = 0
        i = 0
        while i < len(nums):
            length = 1
            if nums[i]-1 in numset:
                i+=1
                continue
            while nums[i]+length in numset:
                length +=1
            longlength = max(length,longlength)
            i+=1
        return longlength