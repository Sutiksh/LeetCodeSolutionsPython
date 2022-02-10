class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        visit = set()
        visit.add(nums[0])
        
        for i in range(1, len(nums)):
            if nums[i] in visit:
                return True
            else:
                visit.add(nums[i])
        return False