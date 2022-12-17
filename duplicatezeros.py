class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        l=0
        size = len(arr)
        while l<size:
            if arr[l]==0:
                arr.insert(l,0)
                l+=2
            else:
                l+=1
        arr[:]=arr[:size]