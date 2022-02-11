class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cnums = []
        i, j = 0, 0
        if len(nums1) == 0:
            cnums = nums2
        elif len(nums2) == 0:
            cnums = nums1
        elif len(nums1) == 0 and len(nums2) == 0:
            return 0
        
        
        if len(nums1) > 0 and len(nums2) > 0:
            while i < len(nums1) and j < len(nums2):
                # print(i, j, len(nums1), len(nums2))
                if nums1[i] <= nums2[j]:
                    cnums.append(nums1[i])
                    i += 1
                else:
                    cnums.append(nums2[j])
                    j += 1


            if i < len(nums1):
                while i < len(nums1):
                    cnums.append(nums1[i])
                    i += 1

            if j < len(nums2):
                while j < len(nums2):
                    cnums.append(nums2[j])
                    j += 1
            
            
        print(cnums)
        mid = len(cnums) // 2
        med = 0
        if len(cnums) % 2 == 0:
            med = (cnums[mid - 1] + cnums[mid]) / 2
        else:
            med = cnums[mid]

        return med