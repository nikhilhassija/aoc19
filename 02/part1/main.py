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


mem = None

with open("input.txt", "r") as file:
	mem = file.read().split(',')

	mem = list(map(int, mem))

	mem[1], mem[2] = 12, 2

for op, in_a, in_b, out in commands(mem):
	if op == 1:
		mem[out] = mem[in_a] + mem[in_b]

	elif op == 2:
		mem[out] = mem[in_a] * mem[in_b]

	elif op == 99:
		break

print(mem[0])
