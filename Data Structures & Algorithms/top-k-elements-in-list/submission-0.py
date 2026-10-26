class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(list)
        for x in nums:
            numdict[x].append(x)
        returnlist = []
        while k > 0:
            maxlen = 0
            maxval = 0
            for list1 in numdict.values():
                if len(list1) > maxlen:
                    maxlen = len(list1)
                    maxval = list1[0]
            numdict.pop(maxval)
            returnlist.append(maxval)
            k-=1
        return returnlist