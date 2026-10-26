class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        print([nums1, nums2])
        for x in nums1[:]:
            if x in nums2:
                nums1.remove(x)
                nums2.remove(x)
                print([nums1, nums2])
        return [nums1, nums2]