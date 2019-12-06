def valid(pw):
	is_valid = True

	is_valid = is_valid and (list(pw) == sorted(pw))
	is_valid = is_valid and (len(set(pw)) < len(pw))

	has_double = False

	for digit in range(10):	
		has_double = has_double or (pw.count(str(digit)) == 2)

	is_valid = is_valid and has_double

	return is_valid

start, end = None, None

with open("input.txt", "r") as file:
	start, end = map(int, file.read().split("-"))

total_pass = 0

for pw in range(start, end + 1):
	if valid(str(pw)):
		total_pass += 1

print(total_pass)
