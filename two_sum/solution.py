class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            n = target - nums[i]
            if n in nums[i+1:]:
                j = nums.index(n, i+1)
                return [i, j]
            else:
                continue