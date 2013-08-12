import sys
import zipfile
import itertools

filename = ""
try:
	filename = sys.argv[1];
except:
	print "The filename was not a valid string"
	exit(1)

#characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
characters = "abcdefghijklmnopqrstuvwxyz"
zipFile = zipfile.ZipFile(filename, "r")

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
			except Exception as e:
				pass

print "no pw found..."
