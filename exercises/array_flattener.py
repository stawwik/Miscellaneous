def flatten(array: list | tuple) -> list:
	"""
	Recursive function for flattening any dimensions of nested arrays.

	Parameters
	----------
	array: list | tuple
		Data meant to be flattened.

	Returns
	-------
	list
		Flattened 1-D list from input array.
	"""

	def recursion(index: int, input_arr: list | tuple, output_arr: list):
		"""Function handling recursion logic."""
		# Making sure current index does not raise error.
		if index >= len(input_arr):
			return  # If end of array is reached, end this function call.

		current_element = input_arr[index]
		# If current element is an array, start recursion in it.
		if isinstance(current_element, (tuple, list)):
			recursion(0, current_element, output_arr)
		else:
		# If not an array, append current element to output.
			output_arr.append(current_element)

		# Step to next element in current array.
		recursion(index + 1, input_arr, output_arr)

	flattened_output = []
	# Start recursive walk through array elements.
	recursion(0, array, flattened_output)

	return flattened_output
