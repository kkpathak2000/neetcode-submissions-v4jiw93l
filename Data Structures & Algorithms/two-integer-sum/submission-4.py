class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = 0
        seen = {}
        for num in nums:
            sum = target - num
            if sum in seen:
                return [seen[sum],index]
            seen[num] = index
            index += 1
