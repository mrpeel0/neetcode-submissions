class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        combined = nums1 + nums2
        combined = set(combined)

        output = [[],[]]
        for x in combined:
            if x in combined and x in nums1 and x in nums2:
                continue
            elif x in combined and x in nums1:
                output[0].append(x)
            else:
                output[1].append(x)
        return output
