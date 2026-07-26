class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trips = []
        n = len(nums)
        nums.sort()
        # while l<r:
        #     for i in range(l,r):
        #         if nums[l]+nums[r]+nums[i] == 0:
        #             if [nums[l],nums[r],nums[i]] not in trips:
        #                 trips.append([nums[l],nums[r],nums[i]])
        #     l+=1
        #     r-=1
        for i in range(n):
            l = i+1
            r = n - 1
            while l< r:
                if nums[i] +nums[l] + nums[r] > 0:
                    r-=1
                elif nums[i] +nums[l] + nums[r] < 0:
                    l+=1
                else:
                    if [nums[l],nums[r],nums[i]] not in trips:
                        trips.append([nums[l],nums[r],nums[i]])
                    l+=1
                    r-=1
        return list(trips)
            
                