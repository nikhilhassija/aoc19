def commands(mem):
	sz = len(mem)
	k = 0

	while k < sz:
		if mem[k] == 99:
			yield 99, 0, 0, 0
			k += 1
		else:
			yield mem[k:k+4]
			k += 4

def check(mem, a, b, target):
	mem[1], mem[2] = a, b

	for op, in_a, in_b, out in commands(mem):
		if op == 1:
			mem[out] = mem[in_a] + mem[in_b]

		elif op == 2:
			mem[out] = mem[in_a] * mem[in_b]

		elif op == 99:
			break

	return (mem[0] == target)

mem = None
target = 19690720

with open("input.txt", "r") as file:
	mem = file.read().split(',')

	mem = list(map(int, mem))

sz = len(mem)

for a in range(sz):
	for b in range(sz):
		if check(mem.copy(), a, b, target):
			print("{:02d}{:02d}".format(a, b))
			exit(0)
