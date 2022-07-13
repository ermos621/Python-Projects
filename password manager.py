from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key" , "wb") as key_file:
        key_file.write(key)


write_key()

#Remove it from the comment for the first time to run the code
and produce a file to encrypt our stored password

'''

def load_key():
    file = open("key.key","rb").read()
    key = file.read()
    file.close()
    return key

'''
master_pwd = input ("What is the master password ? ")
key = load_key() + master_pwd.encode()

#Tried to make a master key to encrypt and decrypt the password
'''

key = load_key()
fer = Fernet(key)

def view():
    with open('passowords.txt','r') as f :
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print ("User : ", user , " | Password" , 
                fer.decrypt(passw.encode()).decode())



def add():
    name = input ("Account name : ")
    pwd = input("Account password: ")

    with open('passowords.txt','a') as f :
        f.write( name +"|"+ fer.encrypt(pwd.encode()).decode() + "\n" )

while True:
    mode = input("Would you like to add a new password or view existing one (view, add), press q to quit ? ").lower
    if mode == "q" :
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue
