# Importing Fernet from Cyrptography Module 
from cryptography.fernet import Fernet

# Creating a Key for encryption and decyption
key = Fernet.generate_key()

# print("Key : ",key)

# Createing a variable to store key
f = Fernet(key)
print("f ",f)

# Creating a token which includes our message
token = f.encrypt(b"Hi My Name is RUTUJA PATIL")

# print("TOKEN : ", token)

# Decrption Data
# print("Decrpyted Data ",f.decrypt(token))



