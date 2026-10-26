class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        outputlist = []
        if len(original) != m*n:
            return outputlist
        rows = 0
        count = 0

        while rows < m:
            outputlist.append([])
            cols = 0
            while cols < n:
                outputlist[rows].append(original[count])
                count += 1
                cols += 1
            rows +=1

        return outputlist   
