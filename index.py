# input:
# original
# encrypted
# to encrypt
# to decrypt

# output:
# encrypted
# decrypted

from cryptor import swap

original_str = input()
encrypted_str = input()
str_to_encrypt = input()
str_to_decrypt = input()

original_to_encrypted = {}
encrypted_to_original = {}

for i in range(len(original_str)):
    original_to_encrypted[original_str[i]] = encrypted_str[i]
    # encrypted_to_original[encrypted_str[i]] = original_str[i]

encrypted_to_original = {value: key for key, value in original_to_encrypted.items()} # invert dictionary for fun

# for readability
def encrypt(str): 
	return swap(original_to_encrypted, str_to_encrypt)

def decrypt(str):
	return swap(encrypted_to_original, str_to_decrypt)

print(encrypt(str_to_encrypt))
print(decrypt(str_to_decrypt))
