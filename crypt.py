import random
import math	

# Caesar Cipher
# Arguments: string, integer
# Returns: string
def encrypt_caesar(plaintext, offset):
	ciphertext = ""
	for char in plaintext:
		ciphertext += chr(ord(char) + offset)
	return ciphertext

# Arguments: string, integer
# Returns: string
def decrypt_caesar(ciphertext, offset):
	plaintext = ""
	for char in ciphertext:
		plaintext += chr(ord(char) - offset)
	return plaintext

# Vigenere Cipher
# Arguments: string, string
# Returns: string
def encrypt_vigenere(plaintext, keyword):
	ciphertext = ""
	for i in range(0, len(plaintext)):
		textchar = plaintext[i]
		keychar = keyword[i % len(keyword)]
		iphertext += chr(ord(textchar) + ord(keychar) - 65)
	return ciphertext

# Arguments: string, string
# Returns: string
def decrypt_vigenere(ciphertext, keyword):
	plaintext = ""
	for i in range(0, len(ciphertext)):
		textchar = ciphertext[i]
		keychar = keyword[i % len(keyword)]
		plaintext += chr(ord(textchar) - ord(keychar) + 65)
	return plaintext

# Merkle-Hellman Knapsack Cryptosystem
# Arguments: integer
# Returns: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
def generate_private_key(n=8):
	W = (random.randint(1,5),)
	total = W[0]
	for i in range(1, n):
		W += (random.randint(total + 1, 2 * total),)
		total += W[i]
	Q = random.randint(total + 1, 2 * total)
	R = 0
	while math.gcd(Q, R) != 1:
		R = random.randint(2, Q - 1)
	return (W, Q, R)

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
	B = ()
	for w_i in private_key[0]:
		B += ((private_key[2] * w_i) % private_key[1],)
	return B

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
	C = []
	for char in plaintext:
		binary_string = bin(ord(char))[2:]
		A = (0,) * (8 - len(binary_string))
		for i in range(0, len(binary_string)):
			A += (int(binary_string[i]),)
		C_char = 0
		for i in range(0, 8):
			C_char += A[i] * public_key[i]
		C.append(C_char)
	return C

# Arguments: integer, integer
# Preconditions: Q >= R, gcd(Q, R) = 1
# Returns: tuple (x, y) where xQ + yR = 1
def euclidean_extended(Q, R):
	if Q % R == 1:
		return (1, (Q // R) * -1)
	next = euclidean_extended(R, Q % R)
	return (next[1], next[0] - next[1] * (Q // R))

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
	S = euclidean_extended(private_key[1], private_key[2])[1]
	plaintext = ""
	for C_char in ciphertext:
		C_prime = (C_char * S) % private_key[1]
		binary_char = ''
		for i in range(len(private_key[0]) - 1, 0, -1):
			w_i = private_key[0][i]
			if w_i > C_prime:
				binary_char = '0' + binary_char
			else:
				binary_char = '1' + binary_char
				C_prime -= w_i
		plaintext += chr(int(binary_char, 2))
	return plaintext
			
		
		

def main():
	private_key = generate_private_key()
	public_key = create_public_key(private_key)
	plaintext = input("Input a message:\n")
	ciphertext = encrypt_mhkc(plaintext, public_key)
	print("Here is your encrypted message:")
	print(encrypt_mhkc(plaintext, public_key))
	print("Here is your decrypted message:")
	print(decrypt_mhkc(ciphertext, private_key))

if __name__ == '__main__':
    main()