def fuel(mass):
	if mass > 0:
		cur_fuel = max((mass // 3) - 2, 0)

		return cur_fuel + fuel(cur_fuel)

	return 0

with open("input.txt", "r") as file:
	total_fuel = 0

	for line in file:
		total_fuel += fuel(int(line))

	print(total_fuel)
