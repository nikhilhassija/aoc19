def fuel(mass):
	return (mass // 3) - 2

with open("input.txt", "r") as file:
	total_fuel = 0
	for line in file:
		total_fuel += fuel(int(line))

	print(total_fuel)
