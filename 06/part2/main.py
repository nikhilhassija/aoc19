orbit_parent = {}

com = "COM"
san = "SAN"
you = "YOU"

def get_ancestry(planet):
	ancestry = []

	while planet != com:
		planet = orbit_parent[planet]

		ancestry.append(planet)

	ancestry.reverse()

	return ancestry

def get_orbit_jumps(planet, target):
	jumps = 0

	parent = orbit_parent[planet]

	while parent != target:
		jumps += 1
		parent = orbit_parent[parent]

	return jumps

with open("input.txt", "r") as file:
	for line in file:
		parent, planet = line.strip().split(")")

		orbit_parent[planet] = parent

ancestry_you = get_ancestry(you)
ancestry_san = get_ancestry(san)

lca = com

for x, y in zip(ancestry_you, ancestry_san):
	if x == y:
		lca = x

	else:
		break

up_jumps = get_orbit_jumps(you, lca)
down_jumps = get_orbit_jumps(san, lca)

print(up_jumps + down_jumps)
