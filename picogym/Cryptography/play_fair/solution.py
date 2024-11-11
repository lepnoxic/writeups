SQUARE_SIZE = 6

def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def decrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]

def decrypt_string(s, matrix):
	result = ""
	if len(s) % 2 == 0:
		plain = s
	else:
		plain = s + "irlgektq8ayfp5zu037nov1m9xbc64shwjd2"[0]
	for i in range(0, len(plain), 2):
		result += decrypt_pair(plain[i:i + 2], matrix)
	return result

key = "irlgektq8ayfp5zu037nov1m9xbc64shwjd2"
enc_msg = "h5a1sqeusdi38obzy0j5h3ift7s2r2"
m = generate_square(key)
print(decrypt_string(enc_msg, m))
