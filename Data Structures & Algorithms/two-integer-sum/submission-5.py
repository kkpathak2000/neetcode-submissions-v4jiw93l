class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index,num in enumerate(nums):
            sum = target - num
            if sum in seen:
                return [seen[sum],index]
            seen[num] = index
