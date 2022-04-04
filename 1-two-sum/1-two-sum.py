class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {} # Create hm for (num, index)
        for i in range(len(nums)):
            comp = target - nums[i] # take difference 
            if comp in hm: # check if difference exist in hm
                return [hm[comp], i] # return index of difference and current
            else:
                hm[nums[i]] = i # else add to hm
        
        return []
        