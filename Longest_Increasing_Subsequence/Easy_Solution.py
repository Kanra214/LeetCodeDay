import bisect
class Solution:
	#Since we only care about the length instead of exact longest increasing subsequence
	#When processing a num thats larger than any element in the list, append it to make the list longer
	#When processing a smaller num, find the position this num x should be inserted to
	#And replace element y in that position
	#Clearly x < y
	#This gives more possibility for the upcomming num to make list longer
	#Even though this breaks the actual longest increasing subsequence
	#[2,8,9,5,6,7]
	#[2,8,9] -->[2,5,6,7]
	
	#[2,8,9,10,5,6,11]
	#[2,8,9,10] -->[2,5,6,10,11] actual subsequence = [2,8,9,10,11]
	#length remains correct
	
	
    def lengthOfLIS(self, nums):
        
        list = []
        for num in nums:
            idx = bisect.bisect_left(list, num)
            if idx == len(list):
                list.append(num)
            else:
                list[idx] = num
        return len(list)