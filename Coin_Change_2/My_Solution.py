def changeHelper(self, amount, coins, last):
	if amount == 0:
		last.insert(0,0)
		return 0
	else:
		k = amount#maximum number of coins
		m = 0
		for vi in coins:
			if k > change(amount-vi,coins, last)+1:
				k = change(amount-vi,coins, last)+1
				m = vi
		last.insert(amount,m)
		return k

	

def change(self, amount, coins):
	last = []
	changeHelper(self, amount, coins, last)
	printResult(last)



	