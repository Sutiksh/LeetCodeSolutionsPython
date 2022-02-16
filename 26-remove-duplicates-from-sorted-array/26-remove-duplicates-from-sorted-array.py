class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        K = 0
        for i in range (1, len(nums)):
            if nums[K] != nums[i]:
                nums[K + 1] = nums[i]
                K+=1
        return (K+ 1)