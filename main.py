import hashlib

inputHash = input("Enter the MD5 hash to crack: ").strip() # Get user input

def crackHash(inputPass): # The inputPass variable gets its value from a user input
    try:
        # Replace the file path with YOUR absolute file path
        passFile = open("C:\\Users\\Duly Florist\\Desktop\\Python Projects\\Password Cracker (Dictionary Attack)\\wordlist.txt", "r") 
        for password in passFile:
            encPass = password.encode("utf-8") # UTF8 Encoding to byte strings from Python strings
            digest = hashlib.md5(encPass.strip()).hexdigest() # Hashes using MD5 Hash and produces hexadecimal in readability form
            if digest == inputPass: 
                print("Password Found: " + password) # Validation if the MD5 Hash matches the password
    except:
        print("Could not find file.") # Exception if the system can't find the file

crackHash(inputHash) # Calls the function
 