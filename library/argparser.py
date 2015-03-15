import argparse
import sys
from xml.etree.ElementTree import parse as elemTree

class MyArgumentParser(argparse.ArgumentParser):
	"""Extend the ArgumentParser"""
	
	def __init__(self, parents=[]):
		super(MyArgumentParser, self).__init__(parents=parents,add_help=False)

	def error(self, message):
	    """error(message: string)
	    IMP : Very tricky override to solve the problem
	    If the error message says "the following arguments are required" , then skip this error and continue
	    This way atleast we get the parsed object which will not contains some of the required arguments
	    For any other type of errors, report error
	    """
	    text = "the following arguments are required"
	    if text in message:
	    	return
	    super(MyArgumentParser,self).error(message)


def parse_args(parser, xml_file = None , args = None):
	""" 
	This function takes the below arguments
	parser : Base ArgumentParser object, where the rules for the parser are defined.
	xml_file : Argument name that corresponds to the XML file which also supplies arguments.
				If this argument is present , this function will parse the given XML file and combine the arguments with the passed args as well.
	args : The ARGS array				
	"""
	# Using the given parser, create a new custom parser
	p = MyArgumentParser(parents= [parser])
	# If user has provided args as parameter use it, else use the command line arguments
	# The first command line argument would be the python file name, skip it
	args = args if args else sys.argv[1:]
	# Parse using custom parser. Custom parser would still return namespace even if some of the parameters are present.
	argsNamespace = p.parse_args(args)
	argsDictionary = argsNamespace.__dict__
	
	# If XML file is given which also can supply arguments, process the same
	if (xml_file != None and argsDictionary[xml_file] != None):
		# Read additional arguments from the XML file
		additionalArgs = __read_additional_args__(argsDictionary, argsDictionary[xml_file])
		# Add the additional arguments from xml file to args
		args.extend(additionalArgs)

	# Parse again and return the new one, but this time parse using the original parser.
	# Any errors about missing required arguments should be reported now
	argsNamespace = parser.parse_args(args)
	return argsNamespace


def __read_additional_args__(dict, xml_file):
	args = []
	try:
		readXmlData = elemTree(source = xml_file)
		for k,v in dict.items():
			# Attempt to read from XML only if the argument doesnt exist in command line
			# Command line arguments have higher priority
			if (v == None):
				v = readXmlData.findtext(k)
				# If the argument exists in xml file, then add it in args array
				args.extend(["--" + k, v]) if v != None else None

	except Exception as e:
		raise (e)
	else:
		pass
	finally:
		pass
		# print (args)

	return args




