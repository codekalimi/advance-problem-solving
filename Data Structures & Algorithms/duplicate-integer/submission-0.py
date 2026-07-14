class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l = 0
        r = len(nums) - 1
        while l < r:
            if nums[l] == nums[r]:
                return True
            else:
                l+=1
        return False
        