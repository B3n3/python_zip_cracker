import sys
import zipfile
import itertools

#characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
characters = "abcdefghijklmnopqrstuvwxyz"
#hardcoded filename - will be changed soon
zipFile = zipfile.ZipFile("fff.zip", "r")

#iterate all possible lengths of the password
for leng in range(1, len(characters)+1):
	print "lenght of password: ", leng

	#create an iterator over the cartesian product of all possible permuations
	it = itertools.product(characters, repeat=leng)

	#iterate all created permutations
	for passw in it:
			try:
				#join the tupel to a string and set the password
				passwd = ''.join(passw)
				zipFile.setpassword(passwd)

				""" 
				try to extract the files from the file
				if the password is wrong, an exception is thrown,
				(RuntimeError), which is caught in the except part
				"""
				zipFile.extractall()

				#if there was no error the password will be shown and the programm exits
				print "The password is: ", passwd
				exit()
			except RuntimeError:
				pass
			except zipfile.BadZipfile:
				pass

print "no pw found..."
