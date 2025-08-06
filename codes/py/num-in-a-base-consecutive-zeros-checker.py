# Checks whether a number has consecutive 0’s in the given base or not

# We first convert to given base, then
# check if the converted number has two
# consecutive 0s or not
def hasConsecutiveZeroes(N, K):
	z = toK(N, K)
	print ( "{} in Base {} => {}".format(N,K,z) )
	if (check(z)):
		print("Yes")
	else:
		print("No")

# Function to convert N into base K
def toK(N, K):

	# Weight of each digit
	w = 1
	s = 0
	while (N != 0):
		r = N % K
		N = N//K
		s = r * w + s
		w *= 10
	return s

# Function to check for consecutive 0
def check(N):

	# Flag to check if there are consecutive 
	# zero or not
	fl = False
	while (N != 0):
		r = N % 10
		N = N//10

		# If there are two consecutive zero 
		# then returning False
		if (fl == True and r == 0):
			return False
		if (r > 0):
			fl = False
			continue
		fl = True
	return True

# Driver code
N, K = int(input("Enter the number:")), int(input("Enter the base:"))
hasConsecutiveZeroes(N, K)
