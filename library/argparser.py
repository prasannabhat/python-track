import argparse
import sys

def parse_args(args = None):
	""" 
	This function takes the command line arguments from the terminal and returns the dictionary corresponds to the arguments
	Refer usage.txt for the argument details
	If any mandatory argument is missing or unsupported value is supplied to any parameter then this method should throw Exception, 
	displaying an appripriate message

	"""
	parser = argparse.ArgumentParser()
	#Positional arguments
	parser.add_argument("command", help= "Command to be executed", choices= ['sync'])

	# Optional arguments , which are optional
	parser.add_argument("-x", "--xml", help=""" XML file which contains the options. Even the Mandatory parameters can be specified in XML file
							If same parameter is present both in command line & XML , command line parameter will be given priority""")
	parser.add_argument("-s", "--sheet" , help = "Worksheet where the data will be written. If not specified query name will be used for this")

	parser.add_argument("-u", "--user", help="User name , required to login to CSCRM",required=True)	
	args = args if args else sys.argv[1:]
	args = parser.parse_args(args)
	argsDictionary = args.__dict__
	return argsDictionary

