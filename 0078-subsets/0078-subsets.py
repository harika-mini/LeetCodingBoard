class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        def inner(nums, path, res):
            for i, el in enumerate(nums):
                inner(nums[i+1:], path + [el], res)
            res.append(path)
        inner(nums, path, res)
        return res