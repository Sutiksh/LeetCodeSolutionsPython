class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=set()
        
        #using two pointer method to each element of list
        for i in range(len(nums)-1):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[i]+nums[r]==0 :
                    #cleaning data from duplicates
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif nums[l]+nums[i]+nums[r]>0:
                    r-=1
                else:
                    l+=1
        #convert to list of lists in return
    
        return list(res)