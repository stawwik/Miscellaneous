# A circular prime is an integer where all rotations of its digits are themselves prime.
# For example, 197 is a circular prime because all rotations of its digits: 197, 971, and 719, are prime numbers.

def is_circular_prime(n: int) -> bool:
	"""
	Checks if given n is a circular prime number.

	Parameters
	----------
	n: int
		Number to be checked.

	Returns
	-------
	bool
		True if n is circular prime, False otherwise.
	"""

	permutations = len(str(n))  # How many loops are needed.
	permutation = 1
	new_n = None

	# Loop for creating new permutations of n and checking them.
	while permutation <= permutations:
		# Border case.
		if new_n is None:  # First permutation
			current_n = str(n)
		else:
			current_n = str(new_n)

		# Starting to check for prime from i=2.
		# If dividable by i -> not a circular prime for any
		# permutation. Can return False without checking rest
		# of permutations.
		i = 2  # n%1 = 0, so loop will always return False.
		num = int(current_n)  # New int var for loop.
		while i < num:  # Always divisible by itself, so i < num.
			if num % i == 0:  # If num is not a prime.
				return False
			i += 1

		# Creating new permutation. First digits is new last digit.
		new_n = current_n[1:] + current_n[0]
		permutation += 1

	# Exited loop, so n must be circular prime.
	return True
