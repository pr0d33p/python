'''
Question:
The divisors of 6 are 1,2,3 and 6. The sum of the squares of these numbers is 1+4+9+36=50. Let sigma2(n) represent the sum of the squares of the divisors of n.
Thus sigma2(6)=50. Let SIGMA2 represent the summatory function of sigma2, that is SIGMA2(n)=∑sigma2(i) for i=1 to n.
The first 6 values of SIGMA2 are: 1,6,16,37,63 and 113. Find SIGMA2(1015) modulo 109.
'''

def sigma2(n):
	a = []
	addtn = 0
	for i in range(1, int(n / 2) + 1):
		if n % i == 0:
			a.append(i)
	a.append(n)
	for num in a:
		addtn += num**2
	return addtn
print "sigma2(" +str(6)+") = "  + str(sigma2(6))


def SIGMA2(n) :
	b = 0
	c = []
	for i in xrange(1, n+1):
		b += sigma2(i)
		c.append(b)
	return b

def LIST(n) :
	b = 0
	c = []
	for i in xrange(1, n+1):
		b += sigma2(i)
		c.append(b)
	return c

print "SIGMA2(" +str(6)+") = " + str(LIST(6))
print "SIGMA2(1015) % 109 = " + str(SIGMA2(1015) % 109)