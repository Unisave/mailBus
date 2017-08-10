import hashlib

def hasher(subber):
	hash_object = hashlib.sha512(subber)
	hex_dig = hash_object.hexdigest()
	return(hex_dig)