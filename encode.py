#!/usr/bin/env python
#
import base64
import getpass

def main():

	user = input("username:")
	if user != None:
		passwd = getpass.getpass("password:")
		if passwd != None:
			print("processing...")
		else:
			print("Blank password not allowed")
	else:
		print("Must set a username and passwd to encode it")

			
	c = base64.b64encode(bytes(user+":"+passwd,"utf-8"))	
	#print(f"base64 encoded: {c.decode("utf-8")}")
	print(c)

if __name__ == '__main__':
	main()
