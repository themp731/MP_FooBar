def answer(coins):
	pads = 0
	remain = coins
	factors = [i for i in range(coins,0,-1) if i**2 <= coins]
	print(factors)
	for f in factors:
		if (remain - f**2) >= 0:
			while remain>=f**2:
				remain = remain - f**2
				pads += 1
	print(pads)
	return(pads)
answer(24)
answer(64)
