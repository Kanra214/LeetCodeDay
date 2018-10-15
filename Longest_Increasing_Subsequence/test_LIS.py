import unittest
from Longest_Increasing_Subsequence import My_Solution


class Test_LIS(unittest.TestCase):
	def test_lengthOfLIS(self):
		ins = My_Solution.Solution()
		nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
		nums2 = [10, 9, 8, 7, 6, 5]
		nums3 = []
		nums4 = [1, 2, 3]
		# result1 = Solution.lengthOfLIS(nums1)
		self.assertEqual(ins.lengthOfLIS(nums1), 4)
		self.assertEqual(ins.lengthOfLIS(nums2), 1)
		self.assertEqual(ins.lengthOfLIS(nums3), 0)
		self.assertEqual(ins.lengthOfLIS(nums4), 3)
	
	if __name__ == '__main__':
		unittest.main()