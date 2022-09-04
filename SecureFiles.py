import sys
from cryptography.fernet import Fernet
import base64

def print_error(message : str):
    print("./SecureFiles.py: Error: {0}".format(message))

def print_incorrect_use_message(message : str):
    print_error("{0}\nExample usage './SecureFiles.py (decrypt|encrypt) key {filename}'".format(message))


def encrypt_files(fernet, filenames):
    
    for filename in filenames:
        plaintext_file = open("./" + filename, "rb")
        plaintext_bytes = plaintext_file.read()
        plaintext_file.close()
        
        ciphertext_file = open("./" + filename + ".ciphertext", "wb")
        ciphertext_file.write(fernet.encrypt(plaintext_bytes))
        ciphertext_file.close()
        
def decrypt_files(fernet, filenames):

    for filename in filenames:            
        ciphertext_file = open("./" + filename + ".ciphertext", "rb")
        ciphertext_bytes = ciphertext_file.read()
        ciphertext_file.close()

        try:
            plaintext = fernet.decrypt(ciphertext_bytes)
        except:
            print_error("Unable to decrypt " + filename)

        plaintext_file = open("./" + filename, "wb")
        plaintext_file.write(plaintext)
        plaintext_file.close()
    

def main():

    if (len(sys.argv) < 3):
        print_incorrect_use_message("Incorrect number of arguments")
        exit(-1)
    elif (sys.argv[1] != 'decrypt' and sys.argv[1] != 'encrypt'):
        print_incorrect_use_message("Second argument must be either 'encrypt' or 'decrypt'")
        exit(-1)
    
    encryption_option = sys.argv[1]
    key = sys.argv[2]
    
    filenames = []
    if (len(sys.argv) > 3):
        for i in range(3, len(sys.argv)):
            filenames.append(sys.argv[i])
    
    try:
        fernet = Fernet(base64.b64encode(bytes(key, "utf-8")))
    except ValueError:
        print_error("Key must be 32 characters long")
        exit(-1)
    
    
    if (encryption_option == 'encrypt'):
        encrypt_files(fernet, filenames)
        
    elif (encryption_option == 'decrypt'):
        decrypt_files(fernet, filenames)

    
      
if __name__ == '__main__':
    main()
    # print(Fernet.generate_key())