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
		ciphertext += chr(ord(textchar) + ord(keychar) - 65)
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
    pass

# Arguments: tuple (W, Q, R) - W a length-n tuple of integers, Q and R both integers
# Returns: tuple B - a length-n tuple of integers
def create_public_key(private_key):
    pass

# Arguments: string, tuple (W, Q, R)
# Returns: list of integers
def encrypt_mhkc(plaintext, public_key):
    pass

# Arguments: list of integers, tuple B - a length-n tuple of integers
# Returns: bytearray or str of plaintext
def decrypt_mhkc(ciphertext, private_key):
    pass

def main():
	print(encrypt_vigenere("DOG", "AB"))
	print(decrypt_vigenere(encrypt_caesar("DOG", "AB"), "AB"))

if __name__ == '__main__':
    main()