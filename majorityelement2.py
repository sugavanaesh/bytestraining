class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=[]
        size = len(nums)
        for i in set(nums):
            if nums.count(i)>size/3:
                res.append(i)
        return res