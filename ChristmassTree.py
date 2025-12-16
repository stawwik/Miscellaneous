# Copyright 2025 stawwik <stawwik@gmail.com>
# MIT License


import sys

import pygame as pg
import random as rng


class Animation:
	"""Class handling animation."""
	def __init__(self):
		# Initialize pygame.
		pg.init()

		# Initialize clock for frame rate handling.
		self.clock = pg.time.Clock()

		# Initialising screen.
		self.screen = pg.display.set_mode((1, 1))
		pg.display.set_caption('Happy Christmas')

		# Creating the tree instance.
		self.tree = Tree(self)
		# Adjusting window size to generated tree.
		self.screen = pg.display.set_mode((self.tree.rect.width,
										  self.tree.rect.height))

	def run(self):
		"""Running the animation"""
		while True:
			# Checking for app exit input.
			self._check_events()

			self.screen.fill(color='#262626')
			self.tree.draw_tree(self.tree.text_lst)

			pg.display.flip()
			self.clock.tick(2)  # Set 1-3 fps.

	def _check_events(self):
		"""Checks keyboard inputs for app exit."""
		for event in pg.event.get():
			if event.type == pg.QUIT:
				sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					sys.exit()


class Tree:
	"""Class used for storing drawing and animating the lights."""
	def __init__(self, anim):
		# Getting screen settings.
		self.screen = anim.screen

		# Characters used for tree building. Len of string has affect on
		# probability of it being used during tree generation.
		self.lights = 'oO'
		self.chars = '#####'
		self.star = '+'
		self.stump = 'H'

		# Lights colors.
		self.lights_colors_tup = ((255, 0, 0), (128, 255, 0),
								  (0, 128, 255), (255, 0, 255))

		# Tree font and font size.
		self.font_size_v = 22
		self.font_size_h = self.font_size_v * 0.6
		self.font = pg.font.SysFont(None, self.font_size_v)

		# Make a tree string representation matrix with given height and
		# segments.
		self.text_lst = self._create_tree_text(20, 4, 2)
		# Get whole tree's rectangle.
		self.rect = self._get_tree_rect()

	def _get_tree_rect(self):
		"""Returns rect of whole tree."""
		fig_h = len(self.text_lst[0]) * self.font_size_v*0.8
		fig_w = self.text_lst[1] * self.font_size_h

		return pg.rect.Rect(0, 0, fig_w, fig_h)

	def _create_tree_text(self, height: int, segments: int, indent: int):
		"""Returns lists of strings for tree image creation"""
		def _stump_width():
			"""Always returns odd width to nicely center stump with tree."""
			width = height // 5
			if width % 2:
				return width
			else:
				return width + 1

		stars = (self.star, 3 * self.star)
		stump = (f'{_stump_width() * self.stump}' for i in range(1, height//4))
		chars = self.chars + self.lights

		# Creating Tree matrix.
		matrix = []
		j = height // segments  # Controls indentation between segments.
		width = 1 + 2*height  # Max len of row w/o indent.
		# Adding star on top.
		for char in stars:
			layer = f'{char:^{width}}'
			matrix.append(layer)
		# Generating and adding tree part.
		for i in range(height):
			n_of_chars = 1 + 2*i - 2*indent*(i // j)
			layer = ''.join(rng.choices(chars, k=n_of_chars))
			matrix.append(f'{layer:^{width}}')
		# Adding stump.
		for row in stump:
			matrix.append(f'{row:^{width}}')

		return matrix, width

	def draw_tree(self, tree_text: tuple[list, int]):
		"""Creates images out of rows of strings paints and draws them."""
		def _painter(s: str):
			if s in self.star:
				return 232, 189, 32
			elif s in self.chars:
				return 50, 150, 50
			elif s in self.lights:
				return rng.choice(self.lights_colors_tup)
			elif s in self.stump:
				return 150, 80, 10
			else:
				return 255, 255, 255

		# Setting characters spacing.
		delta_y = int(self.font_size_v * 0.8)
		delta_x = int(self.font_size_h)

		# Make sprites of individual characters and add them to sprite group.
		for row_index, row in enumerate(tree_text[0]):
			for char_index, char in enumerate(row):
				# Create image out of character (string).
				image = self.font.render(char, True, _painter(char))
				# Position image at coordinates.
				image_rect = image.get_rect()
				image_rect.topleft = (char_index * delta_x, row_index * delta_y)
				# Draw character in image_rect coordinates.
				self.screen.blit(image, image_rect)


if __name__ == '__main__':
	anim = Animation()
	anim.run()
