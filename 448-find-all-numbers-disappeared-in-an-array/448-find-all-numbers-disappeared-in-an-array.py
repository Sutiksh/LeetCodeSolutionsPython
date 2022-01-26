class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        allNums = [i for i in range(1, len(nums) + 1)]
        print(allNums)
        allNumsSet = set(allNums)
        numsSet = set(nums)
        
        diff = allNumsSet.difference(numsSet)
        print(diff)
        
        return list(diff)
        