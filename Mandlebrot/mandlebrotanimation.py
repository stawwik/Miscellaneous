# Copyright 2025 stawwik <stawwik@gmail.com>
# MIT License


import numpy as np
import matplotlib.pyplot as plt

import pathlib

# Setting parameters (these values can be changed).
N = 1280  # Generated plot resolution.
x_domain = np.linspace(-2, 2, N)
y_domain = np.linspace(-2, 2, N)
bound = 2
max_iterations = 64  # any positive integer value.
colormap = "inferno"  # set to any matplotlib valid colormap.

def func(z, p, c):
	return z**p + c

# Computing 2D array to represent the Mandelbrot set.
r = range(100, 310, 5)
n_i = len(r)
for n, i in enumerate(r):
	p = i / 100
	iteration_array = []
	for y in y_domain:
		row = []
		for x in x_domain:
			z = 0
			c = complex(x, y)
			for iteration_number in range(max_iterations):
				if abs(z) >= bound:
					row.append(iteration_number)
					break
				else:
					try:
						z = func(z, p, c)
					except (ValueError, ZeroDivisionError):
						z = c
			else:
				row.append(0)

		iteration_array.append(row)

	# Plotting the data
	fig, ax = plt.subplots()
	ax.set_aspect("equal")
	graph = ax.pcolormesh(x_domain, y_domain, iteration_array,
						  cmap=colormap)
	fig.colorbar(graph)
	ax.set_title(r'Mandelbrot set: $z_{k+1} = z^{p}_{k} + c$' + fr'. $p=${p:.2f}')
	ax.set_xlabel("Real-Axis")
	ax.set_ylabel("Imaginary-Axis")

	# Saving animation frame. Might want to change path and leave file name.
	path = pathlib.Path(fr'C:\Users\User\Pictures\Mandlebrot\p_{p:.2f}.png')
	plt.savefig(path, dpi=300, format='png') # Saving plot at path.
	plt.close(fig)  # Freeing memory.

	# Printing frame generation status to console.
	done = (n + 1) * 10 // n_i
	print(f'File {path.name} [{done*'■'}{(10-done) * '_'}] {n + 1}/{n_i} done!')
# Now make a gif from generated frames in other program!