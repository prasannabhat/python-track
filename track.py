from library import argparser as parse

try:
	args = parse.parse_args()
except BaseException as e:
	pass
	# print(e)
else:
	print (args)

