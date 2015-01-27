from library import argparser as parse
args = {}

try:
	args = parse.parse_args()
except BaseException as e:
	pass
	# print(e)
else:
	pass
finally:
	print (args)

