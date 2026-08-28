class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        contains = {}
        for num in nums:
            if num in contains:
                return True
            else:
                contains[num] = 0
        return True