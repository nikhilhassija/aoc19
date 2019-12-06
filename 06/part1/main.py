orbit_parent = {}
com = "COM"

with open("input.txt", "r") as file:
	for line in file:
		parent, planet = line.strip().split(")")

		orbit_parent[planet] = parent

planets = orbit_parent.keys()

direct = len(planets)
indirect = 0

for planet in planets:
	parent = orbit_parent[planet]

	while parent != com:
		indirect += 1
		parent = orbit_parent[parent]

print(direct + indirect)
