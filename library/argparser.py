import argparse
import sys

class MyArgumentParser(argparse.ArgumentParser):
	"""docstring for MyArgumentParser"""
	def __init__(self, parents=[]):
		super(MyArgumentParser, self).__init__(parents=parents,add_help=False)


def parse_args(parser, xml_file = None , args = None):
	""" 
	This function takes the below arguments
	parser : Base ArgumentParser object, where the rules for the parser are defined.
	xml_file : Argument name that corresponds to the XML file which also supplies arguments.
				If this argument is present , this function will parse the given XML file and combine the arguments with the passed args as well.
	args : The ARGS array				
	"""
	p = MyArgumentParser(parents= [parser])
	args = args if args else sys.argv[1:]
	args = p.parse_args(args)
	argsDictionary = args.__dict__
	return args

