import bisect


class Solution:
	class ListNode:
		def __init__(self, value):
			self.value = value
			self.next = []
			self.MaxDegree = 1
		
		# self.isEnd = True
		
		def add_next(self, nextNode):
			self.next.append(nextNode)
			# nextNode.isEnd = False
			if nextNode.MaxDegree + 1 > self.MaxDegree:
				self.MaxDegree = nextNode.MaxDegree + 1
		
		def takeMax(node):
			return node.MaxDegree
	
	def lengthOfLIS(self, nums):
		
		maxNumber = 0
		if nums == []:
			return maxNumber
		# nodeList = []
		
		list1 = []
		list2 = []
		
		for num in nums:
			current = Solution.ListNode(num)
			# for node in nodeList:
			
			i = -1
			while i > (-1) * len(list1) - 1:
				node = list2[i]
				if node.value < current.value:
					current.add_next(node)
					break
				i -= 1
			# list2.append(current)
			# list1.append(current.MaxDegree)
			# list.sort(key = Solution.ListNode.takeMax,reverse = True)
			# nodeList.append(current)
			# i used two lists because it seems that bisect cant insort a tuple with incomparable objects
			idx = bisect.bisect_left(list1, current.MaxDegree)
			list1.insert(idx, current.MaxDegree)
			list2.insert(idx, current)
			
			# bisect.insort_left(list,(current.MaxDegree,current))
			if maxNumber < current.MaxDegree:
				maxNumber = current.MaxDegree
		return maxNumber
