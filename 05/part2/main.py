mem = None
ip = 0

def get_mem():
	global ip, mem

	assert(ip < len(mem))

	cur_mem = mem[ip]
	ip += 1

	return cur_mem

def get_cmd():
	cmd = get_mem()

	op_code = cmd % 100

	m1 = (cmd // 10 ** 2) % 10
	m2 = (cmd // 10 ** 3) % 10
	m3 = (cmd // 10 ** 4) % 10

	return op_code, m1, m2, m3

def commands():
	while True:
		cmd, *modes = get_cmd()
		
		yield cmd, *modes

		if cmd == 99:
			break

def add(v1, v2):
	return v1 + v2

def mul(v1, v2):
	return v1 * v2

def jit(v1, v2):
	global ip

	if (v1):
		ip = v2

def jif(v1, v2):
	global ip

	if (v1 == 0):
		ip = v2

def lt(v1, v2):
	return 1 if v1 < v2 else 0

def eq(v1, v2):
	return 1 if v1 == v2 else 0

def exec_cmd(cmd, modes):
	if cmd in [1, 2]:
		params = [get_mem() for i in range(3)]

		v1, v2 = [params[i] if modes[i] else mem[params[i]] for i in range(2)]

		v3 = params[2]

		func = add if cmd == 1 else mul

		mem[v3] = func(v1, v2)

	elif cmd == 3:
		param = get_mem()

		mem[param] = int(input("input: "))

	elif cmd == 4:
		param = get_mem()

		val = param if modes[0] else mem[param]

		print("output:", val)

	elif cmd in [5, 6]:
		params = [get_mem() for i in range(2)]

		v1, v2 = [params[i] if modes[i] else mem[params[i]] for i in range(2)]

		func = jit if cmd == 5 else jif

		func(v1, v2)

	elif cmd in [7, 8]:
		params = [get_mem() for i in range(3)]

		v1, v2 = [params[i] if modes[i] else mem[params[i]] for i in range(2)]

		v3 = params[2]

		func = lt if cmd == 7 else eq

		mem[v3] = func(v1, v2)

	elif cmd == 99:
		exit(0)

	else:
		print("invalid command", cmd)
		assert(False)

with open("input.txt", "r") as file:
	mem = file.read().split(',')

	mem = list(map(int, mem))

for cmd, *modes in commands():
	exec_cmd(cmd, modes)
