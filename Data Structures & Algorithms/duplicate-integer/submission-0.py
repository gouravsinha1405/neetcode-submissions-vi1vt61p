class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dupes = set()

        for i in range(len(nums)):
            if nums[i] in dupes:
                return True
            dupes.add(nums[i])
        return False
        