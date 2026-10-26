class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max = 0
        start = 0
        end = len(heights)-1
        while start < end:
            print(min(heights[start], heights[end]) * (end-start))
            if max < min(heights[start], heights[end]) * (end-start):
                max = min(heights[start], heights[end]) * (end-start)
            if heights[start] < heights[end]:
                start +=1
            else:
                end -=1
        return max