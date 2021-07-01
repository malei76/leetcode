import unittest

from two_sum.solution import Solution

class TestSolution(unittest.TestCase):
    def test_case1(self):
        nums = [2,7,11,15]
        target = 9
        answer = [0, 1]
        self.calc(nums, target, answer)

    def test_case2(self):
        nums = [3, 2, 4]
        target = 6
        answer = [1, 2]
        self.calc(nums, target, answer)

    def test_case3(self):
        nums = [3, 3]
        target = 6
        answer = [0, 1]
        self.calc(nums, target, answer)

    def calc(self, nums, target, answer):
        [a, b] = Solution().twoSum(nums, target)
        self.assertEqual(target, nums[a] + nums[b])
        self.assertEqual([a,b], answer)


#if __name__ == '__main__':
#    unittest.main()
