import hashlib

def generate_password(word):
    hash_object = hashlib.sha256(word.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig[:8]

word = input("Digite: ")
password = generate_password(word)
print("Senha:", password)