import sys
import zipfile
import itertools
import string


# zipfn : zip-file-name, 
# chars : are list of chars that can be used in generation of password
# max_len : maximum length of password to try
def crack_pw(zipfn, max_len, chars = string.ascii_lowercase):
	for length in range(max_len+1):

		# passwords generated using cartesians product, to given length
		pools = itertools.product(chars, repeat = length)

		# Try each generated password
		for pool in pools:
			passwd = bytes("".join(pool))

			# If contents are successfully extracted, password is valid
			# If Runtime Error is caught then password in Invalid, thus try next
			try:
				zipfn.extractall(pwd=passwd)
				return passwd
			except RuntimeError:
				continue

	# Flag for password not found
	return False


# UI
file_name = ""
try:
	file_name = sys.argv[1]
	zip_file = zipfile.ZipFile(file_name, "r")
except (IOError, Exception):
	print("File not found! Try another valid string!")
	sys.exit(1)

print("..Try all possible password combinations!\n Keep Patience!")
recovered_passwd = crack_pw(zip_file, 16)
zip_file.close()

if not recovered_passwd:
	print("\n  > No password found! Try expanding character set!")
else:
	print("\n  > Password for %s: %s" %(file_name, recovered_passwd))
sys.exit(0)
