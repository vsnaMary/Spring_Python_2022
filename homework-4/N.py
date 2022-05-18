class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        for i,n in enumerate(nums):
            m[n] = i
        for i,n in enumerate(nums):
            if target-n in m and m[target-n] != i:
                return [i, m[target-n]]
            