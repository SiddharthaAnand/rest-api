import os

def read_credential(file_name=None):

	_file = open(file_name, "r")
	_lines = _file.readlines()
	_file.close()
	#print _lines
	user_name = _lines[0].strip().split()[1]
	pwd = _lines[1].strip().split()[1]
	url = _lines[2].strip().split()[1]
	print user_name, pwd, url

read_credential("credentials")