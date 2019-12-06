def valid(pw):
	is_valid = True

	is_valid &= (list(pw) == sorted(pw))
	is_valid &= (len(set(pw)) < len(pw))

	return is_valid

start, end = None, None

with open("input.txt", "r") as file:
	start, end = map(int, file.read().split("-"))

total_pass = 0

for pw in range(start, end + 1):
	if valid(str(pw)):
		total_pass += 1

print(total_pass)
