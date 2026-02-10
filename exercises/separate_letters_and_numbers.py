def separate_letters_and_numbers(s: str, sep: str, ign_space=True) -> str:
	"""
	Function separating letters, numbers and special characters in given
	string.

	Parameters
	----------
	s: str
		Input string.
	sep: str
		Character used for separation.
	ign_space: bool
		Flag whether to ignore space character.

	Returns
	-------
	str
		String with separator inserted between letters, numbers and special
		chars.

	"""

	# Making a list out of string for ease of inserting hyphen.
	string_list = list(s.lstrip())
	for index, element in enumerate(string_list):
		# Initializing first state of (is_letter, is_number).
		if index == 0:
			last_state = (element.isalpha(), element.isnumeric())
			# Moving to next element.
			continue

		# Checking if current element (is_letter, is_number).
		current_state = (element.isalpha(), element.isnumeric())

		# Suppress insertion of separator before and after ` `.
		if ign_space:
			if (element == ' ') or (string_list[index-1] == ' '):
				# Updating state to avoid separator after ` `.
				last_state = current_state
				continue

		# If state changed, insert separator at current index.
		if current_state != last_state:
			string_list.insert(index, sep)

		# Update last_state.
		last_state = current_state

	return ''.join(string_list)
