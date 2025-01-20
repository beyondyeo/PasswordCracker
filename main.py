import hashlib

def crackHash(inputPass):
    try:
        passFile = open("C:\\Users\\Duly Florist\\Desktop\\Python Projects\\Password Cracker (Dictionary Attack)\\wordlist.txt", "r") 
        for password in passFile:
            encPass = password.encode("utf-8")
            digest = hashlib.md5(encPass.strip()).hexdigest()
            if digest == inputPass:
                print("Password Found: " + password)
    except:
        print("Could not find file.")


if __name__ == '__main__':
    inputHash = input("Enter the MD5 hash to crack: ").strip()
    crackHash(inputHash)

