def lengthOfLIS(self, nums):
	table = []
	last = []
	if nums == []:
		return 0
	for i in range(len(nums)):
		if i == 0:
			table.append(1)
			last.append(nums[i])
		else:
			if nums[i] > max(last):
				table.append(max(table) + 1)
				last.append(nums[i])
			elif nums[i] <= min(last):
				
				while 1 in table:
					delID = table.index(1)
					table.pop(delID)
					last.pop(delID)
				table.append(1)
				last.append(nums[i])
			
			
			else:#case 3: find the longest list with last is < nums[i]
			
				smallerThanNewNumber = []
				for j in range(len(table)):
					if last[j] < nums[i]:
						smallerThanNewNumber.append((table[j], j))
				maxLength = max(smallerThanNewNumber)
				maxID = maxLength[1]
				
				length = table[maxID] + 1
				while length in table:
					delID = table.index(length)
					table.pop(delID)
					last.pop(delID)
				table.append(length)
				last.append(nums[i])
	return max(table)