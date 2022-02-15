import sys
from getpass import getpass

from argon2 import PasswordHasher
ph = PasswordHasher()


def checkPasswordStrength(p):
    if len(p) < 6 or p.islower() or p.isupper() or not(any(i.isdigit() for i in password)):
        print("Password must be longer than 6 characters, must contain at least one lowercase, one uppercase and one "
              "digit!")
        exit()


try:
    ################
    ###    ADD  ####
    ################
    if sys.argv[1] == "add":
        f = open("passwords.txt", "a") # creating
        # f.close()
        if len(sys.argv) == 3:
            users = []
            f = open("passwords.txt", "r")
            lines = f.readlines()
            f.close()
            for line in lines:
                splitted = line.split(chr(29))
                users.append(splitted[0])
            # print(users)
            if sys.argv[2] in users:
                print("Username taken!")
                exit(0)

            # adding user
            password = getpass()
            checkPasswordStrength(password)
            repeat = getpass("Repeat password: ")
            if password != repeat:
                print("User add failed, password mismatch!")
                exit(0)
            hash = ph.hash(password)
            writeString = ""
            writeString += sys.argv[2]
            writeString += chr(29)
            writeString += hash
            writeString += chr(29)
            writeString += "0"

            f = open("passwords.txt", "a")
            f.write(writeString)
            f.write("\n")
            f.close()
            print("User added!")
            exit()
        else:
            print("Wrong input format! Try: add my_username")

    ################
    ### PASSWD  ####
    ################
    if sys.argv[1] == "passwd":
        if len(sys.argv) == 3:
            f = open("passwords.txt", "r")
            lines = f.readlines()
            f.close()
            users = []

            for i in range(0, len(lines)):
                splitted = lines[i].split(chr(29))
                users.append(splitted[0])

            if sys.argv[2] not in users:
                print("User does not exist!")
                exit()
            index = users.index(sys.argv[2])

            old = lines[index].split(chr(29))
            password = getpass()
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
            writeString += sys.argv[2]
            writeString += chr(29)
            writeString += hash
            writeString += chr(29)
            writeString += "0"

            lines[index] = writeString
            f = open("passwords.txt", "w")
            for line in lines:
                f.write(line)

            f.close()
            print("Password changed.")
            exit()

        else:
            print("Wrong input format! Try: passwd my_username")

    ################
    ## FORCEPASS ###
    ################
    if sys.argv[1] == "forcepass":
        if len(sys.argv) == 3:
            users = []
            f = open("passwords.txt", "r")
            lines = f.readlines()
            f.close()
            users = []

            for i in range(0, len(lines)):
                splitted = lines[i].split(chr(29))
                users.append(splitted[0])

            if sys.argv[2] not in users:
                print("User does not exist!")
                exit()
            index = users.index(sys.argv[2])

            lines[index] = lines[index][0:len(lines[index])-2] + "1"
            f = open("passwords.txt", "w")
            for line in lines:
                f.write(line)
            f.close()
            print("User will be required to change password.")
            exit()
        else:
            print("Wrong input format! Try: forcepass my_username")

    ################
    ###    DEL   ###
    ################
    if sys.argv[1] == "del":
        if len(sys.argv) == 3:
            users = []
            f = open("passwords.txt", "r")
            lines = f.readlines()
            f.close()
            users = []

            for i in range(0, len(lines)):
                splitted = lines[i].split(chr(29))
                users.append(splitted[0])

            if sys.argv[2] not in users:
                print("User does not exist!")
                exit()
            index = users.index(sys.argv[2])

            del lines[index]
            f = open("passwords.txt", "w")
            for line in lines:
                f.write(line)

            f.close()
            print("User deleted.")
            exit()
        else:
            print("Wrong input format! Try: forcepass my_username")

except Exception as e:
    print("Input failed!")
    #print(e)