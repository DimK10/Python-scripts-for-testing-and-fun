# This code is intended to help anyone who 
# may want to use hashlib to find hash for
# file given.Hope this helps.

import hashlib
 
file = "C:/Users/<user>/<path_to_file>" #Give the path of the file you need to find hash

h = hashlib.sha256() #hashlib.algorithms on shell gives a tuple that shows all the hash algorithms supported by hashlib

# h = hashlib.sha512() for sha512
# h = hashlib.sha1() for sha-1
# h = hashlib.md5 for md5

with open (file,'rb') as f:

# use chunks of 1024 bytes to calculate the whole hash
	chunk = 0
	while chunk !=b'': #end of bytes
		h.update(chunk) #update the hash with the chunk
	print("sha256: " + h.hexdigest())#return the digest of chunks passed to update() method overall as hexadecimal digits
