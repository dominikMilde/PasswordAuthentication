import sys
from getpass import getpass

from argon2 import PasswordHasher


def checkPasswordStrength(p):
    if len(p) < 6 or p.islower() or p.isupper() or not(any(i.isdigit() for i in password)):
        print("Password must be longer than 6 characters, must contain at least one lowercase, one uppercase and one "
              "digit!")
        exit()


def success(needToChange, lines, old):
    if needToChange:
        password = getpass("You need to enter new password: ")
        try:
            ph.verify(old[1], password)
            print("New password is same as old! Write new password!")
            exit()
        except Exception:
            pass
        checkPasswordStrength(password)
        repeat = getpass("Repeat password: ")
        if password != repeat:
            print("User add failed, password mismatch!")
            exit(0)

        hash = ph.hash(password)
        writeString = ""
        writeString += sys.argv[1]
        writeString += chr(29)
        writeString += hash
        writeString += chr(29)
        writeString += "0"

        lines[index] = writeString
        f = open("passwords.txt", "w")
        for line in lines:
            f.write(line)
        f.close()
    print("Login successful.")
    exit()



def possibleAttack():
    print("POSSIBLE ATTACK ON BASE - calling NSA (not really)")
    # moguce dodati dodatnu obranu, blokiranje i sl.
    exit()


ph = PasswordHasher()
usernameCorrect = False
needToChangePass = False

f = open("passwords.txt", "r")
lines = f.readlines()
f.close()
users = []

for i in range(0, len(lines)):
    splitted = lines[i].split(chr(29))
    users.append(splitted[0])

hash = None

if sys.argv[1] in users:
    usernameCorrect = True
    index = users.index(sys.argv[1])
    old = lines[index].split(chr(29))
    hash = old[1]
    if old[2].strip() == "1":
        needToChangePass = True

for i in range(3):
    password = getpass()
    if usernameCorrect:
        try:
            r = ph.verify(hash, password)
            #print(r)
            success(needToChangePass, lines, old)  # this function will exit
        except Exception as e:
            print("Invalid username or password")
            #print(e)
            continue
    else:
        print("Invalid username or password")

possibleAttack()

