from itertools import islice, product

def walk(start, wire):
	x, y = start

	for command in wire.split(","):
		direction, steps = command[0], int(command[1:])

		for _ in range(steps):
			x += (1 if direction == "U" else 0)
			x += (-1 if direction == "D" else 0)

			y += (1 if direction == "L" else 0)
			y += (-1 if direction == "R" else 0)

			yield x, y

points_a = None
points_b = None

center = (0, 0)

with open("input.txt", "r") as file:
	wire_a = file.readline()
	wire_b = file.readline()

	points_a = [point for point in walk(center, wire_a)]
	points_b = [point for point in walk(center, wire_b)]

dist_a = {}
dist_b = {}

for ind, point in enumerate(points_a):
	if point not in dist_a:
		dist_a[point] = ind + 1

for ind, point in enumerate(points_b):
	if point not in dist_b:
		dist_b[point] = ind + 1

common_points = set(points_a) & set(points_b)

dists = []

for point in common_points:
	dists.append(dist_a[point] + dist_b[point])

print(min(dists))
