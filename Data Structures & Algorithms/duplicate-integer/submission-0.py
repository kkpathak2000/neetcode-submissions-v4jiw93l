class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_set = set(nums)
        if len(nums) > len(list_set):
            return True
        else:
            return False