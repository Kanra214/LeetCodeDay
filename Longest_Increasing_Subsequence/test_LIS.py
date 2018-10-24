import unittest
from Longest_Increasing_Subsequence import DP_Solution


class Test_LIS(unittest.TestCase):
	def test_lengthOfLIS(self):
		# ins = DP_Solution.Solution()
		nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
		nums2 = [10, 9, 8, 7, 6, 5]
		nums3 = []
		nums4 = [1, 2, 3]
		nums5 = [10,9,2,5,3,4]
		nums6 = [2,2]
		nums7 = [10,9,2,5,3,7,200,18,101,102,103]
		# result1 = Solution.lengthOfLIS(nums1)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums1), 4)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums2), 1)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums3), 0)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums4), 3)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums5), 3)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums6), 1)
		self.assertEqual(DP_Solution.lengthOfLIS(self, nums7), 7)

		


	if __name__ == '__main__':
		unittest.main()