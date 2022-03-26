class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, left, right = 0, 0, 1
        length = len(nums)
        if length < 3:
            return length
        while right < length:
            if nums[right] == nums[left]:
                if left == prev:
                    left += 1
                    nums[left] = nums[right]
            else:
                left += 1
                nums[left] = nums[right]
                prev = left
            right += 1
        return left + 1