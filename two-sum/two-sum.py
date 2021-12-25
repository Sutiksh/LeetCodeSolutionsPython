class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        
#         for n in nums:
#             comp = target - n
#             if comp in hm:
#                 return [hm[comp], nums.index(n)]
            
#             else:
#                 hm[n] = nums.index(n)
                
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hm:
                return [hm[comp], i]
            else:
                hm[nums[i]] = i
        
        return []
        