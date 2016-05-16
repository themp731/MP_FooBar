rabbits = {0:1,1:1,2:2}
'''
def breed2(n):
    if n in rabbits:
        return rabbits[n]
    x = n // 2
    if x*2 == n:
        rabbits[n] = breed2(x) + breed2(x + 1) + (x)
    else:
        rabbits[n] = breed2(x - 1) + breed2(x) + 1
    return rabbits[n]
'''

def breed3(n):
    if n in rabbits:
    	return rabbits[n]
    if n not in rabbits:
        # divide n by two for the factor of 2 "R" formulae
        x = n >> 1

        if n & 1:
            # odd, so follow R(2n+1)
            rabbits[n] = R(x) + R(x - 1) + 1
        else:
            # even, so follow R(2n)
            rabbits[n] = R(x) + R(x + 1) + x

    return rabbits[n]
    
#Kept getting MemoryError so copied binary search function
'''
def search(pop):
    time = None
    for n in rabbits:
        if rabbits[n] == pop:
            time = n
    return time
'''

def search2(a, b, target, parity):
	#If we've hit above our goal pop
	if b<=a:
		return None
	
	#Establishing Binary Search Midpoint
	#Caution this is a bitwise function
	n = a + ((b-a) >> 1)

	n += parity != n & 1

	S = breed2(n)

	if S == target:
		return S

	if S>target:
		b = n-1

	else:
		a=n+1
	return search2(a,b,target,parity)

'''
def answer(str_S):
    pop = int(str_S,10)
    n=0
    while breed2(n//2)<pop:
        a = breed2(n)
        n+=1
    result = search(pop)
    return result
'''
def answer(str_S):
	pop = int(str_S,10)
	return search2(0, pop, pop, 1) or search2(0, pop, pop, 0)

print(answer("101"))