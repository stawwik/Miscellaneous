def tic_tac_toe(board: list[list]) -> str:
	"""
	Checks board of tic-tac-toe game for winning player.

	Parameters
	----------
	board: list[list]
		An array representing finished game.

	Returns
	-------
	str
		String, where first letter is game winning character.
	
	Notes
	-----
		Function could use an input validation.
	"""

	# Tuple of winning sets.
	win_conditions = ({'O'}, {'X'})
	# Board dimensions w x h.
	width, height = len(board), len(board[0])
	# Containers for diagonals.
	diagonal_1, diagonal_2 = [], []

	# Iteration through whole board.
	for row_index in range(width):
		# Checking current row.
		row = board[row_index]
		if set(row) in win_conditions:
			return f'{row[0]} wins'

		column = []
		# Iterating through diagonal in reverse with n.
		for col_index, n in enumerate(range(height - 1, -1, -1)):
			# Creating a column.
			column.append(board[col_index][row_index])

			# Creating diagonals.
			if row_index == col_index:
				diagonal_1.append(board[row_index][col_index])
				diagonal_2.append(board[row_index][n])

		# Checking current column.
		if set(column) in win_conditions:
			return f'{column[0]} wins'

	# Search in diagonals.
	if set(diagonal_1) in win_conditions:
		return f'{diagonal_1[0]} wins'
	elif set(diagonal_2) in win_conditions:
		return f'{diagonal_2[0]} wins'

	# No winning conditions met -> must be a draw.
	return 'Draw'
