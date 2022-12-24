class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        s=0
        for f in range(l):
            if nums[f]!=0 and nums[s]==0:
                nums[f],nums[s] = nums[s],nums[f]
            if nums[s]!=0:
                s+=1