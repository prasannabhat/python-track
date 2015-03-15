from helpers import helper
from library import argparser as parse

args = {}

parser = helper.get_parser()

try:
	args = parse.parse_args(parser, xml_file='xml')
except BaseException as e:
	pass
	print(e)
else:
	pass
finally:
	pass
	print (args)

