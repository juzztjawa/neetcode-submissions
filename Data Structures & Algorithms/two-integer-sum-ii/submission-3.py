class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        n = len(numbers)
        r = n - 1
        while l < r:
            if target > numbers[l] + numbers[r]:
                l+=1
            elif target < numbers[l] + numbers[r]:
                r -= 1
            else:
                return [l+1,r+1]

