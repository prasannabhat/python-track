import argparse
import sys


def get_parser():
	"""
	This function gives parser for this specific problem of CSCRM Track
	"""
	parser = argparse.ArgumentParser()
	#Positional arguments
	parser.add_argument("command", help= "Command to be executed", choices= ['sync'])

	# Mandatory arguments
	parser.add_argument("-f", "--file", help=""" Excel file to write the data""", required=True)
	parser.add_argument("-u", "--user", help="User name , required to login to CSCRM",required=True)
	parser.add_argument("-p", "--password" , help="Password for CSCRM", required=True)
	parser.add_argument("-q", "--query" , help="Query which should be run to fetch the data from", required=True)
	parser.add_argument("-sk", "--sync-key" , help="Primary key for syncing. If there are multiple keys seperate them using :", required=True)

	# Optional arguments , which are optional
	parser.add_argument("-x", "--xml", help=""" XML file which contains the options. Even the Mandatory parameters can be specified in XML file
							If same parameter is present both in command line & XML , command line parameter will be given priority""")
	parser.add_argument("-s", "--sheet" , help = "Worksheet where the data will be written. If not specified query name will be used for this")
	return parser
