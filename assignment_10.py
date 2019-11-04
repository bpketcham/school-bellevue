import os

print("Welcome to the Address Book")

userdir = str(input("Please type the directory that you would like to use: "))

if(os.path.isdir(userdir)):
    print("This is a valid directory")
else:
    print("The directory provided does not exist, so it will be created")
    os.mkdir(userdir)

userfile = str(input("Please enter the file name you would like to use: "))
fullfile = userfile + ".txt"

name = str(input("Please enter your name: "))
address = str(input("Please enter your address: "))
phone = str(input("Please enter your phone number: "))

newrecord = name + "," + address + "," + phone

with open(fullfile, 'a') as fileHandle:
	fileHandle.write(newrecord + '\n')
	
print("Your information has been added to address book file: " +
	userfile)
	
with open(fullfile, 'r') as readObject:
	for line in readObject:
		print(line.strip())
