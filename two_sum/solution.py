class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            n = target - nums[i]
            try:
                j = nums.index(n, i+1)
                return [i, j]
            except:
                continue