import re

def parse_inline_code(markdown: str) -> str | None:
	"""
	Function inserting html code tags into markdown string.

	Parameters
	----------
	markdown : str
		String having at least two markdown '`' symbols for inline code.

	Returns
	-------
	html : str or None
		String with html tags in place of markdown's '`' or None if there
		were no inline code in passed markdown string.
	"""
	# Prepare string for substitution.
	html = markdown[:]

	# Compile regex and find all inline code in passed parameter.
	pattern = re.compile(r'`.+?`')
	matches = re.findall(pattern, markdown)

	if matches is not None:
		for match in matches:
			tagged = ''.join(['<code>', match[1:-1], '</code>'])
			# Substitute html tags. count=1 so we don't accidentally
			# substitute duplicate matches from list.
			html = re.sub(pattern, tagged, html, count=1)
		return html
	else:
		return None
