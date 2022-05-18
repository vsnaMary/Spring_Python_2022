from bisect import bisect_left
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        for k,n in enumerate(sorted_nums):
            d = target - n
            i = bisect_left(sorted_nums,d,k+1)
            if  i<len(nums) and sorted_nums[i] == d:
                j = nums.index(n)
                i = len(nums) - nums[::-1].index(d) - 1
                return [i,j]
            
            