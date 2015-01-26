import random
import unittest
import sys
from library import argparser as parse

print ("Command line argumenrs are ", sys.argv)
class TestSequenceFunctions(unittest.TestCase):

    @staticmethod
    def addPositionalArguments(args):
        args.extend(['sync'])

    @staticmethod
    def addMandatoryOptionalArguments(args):
        args.extend(['--user', 'name'])

    @staticmethod
    def removeOptionalArgument(args,param):
        i = args.index(param)
        args[i:i+2] = []
    
    @staticmethod
    def addAllMandatoryArguments(args):
        TestSequenceFunctions.addPositionalArguments(args)
        TestSequenceFunctions.addMandatoryOptionalArguments(args)

    def setUp(self):
        self.args = []
        TestSequenceFunctions.addAllMandatoryArguments(self.args)

    def test_command_1(self):
        # command option is called with sync
        args = []
        TestSequenceFunctions.addMandatoryOptionalArguments(args)
        args.extend(['sync'])
        argsDict = parse.parse_args(args)
        self.assertTrue(argsDict['command'] == 'sync')

    def test_command_2(self):
        # Mandatory option command not present
        args = []
        with self.assertRaises(BaseException):
            parse.parse_args(args)
    
    def test_command_3(self):
        # command option is called with value other than sync
        args = ['calc']
        with self.assertRaises(BaseException):
            parse.parse_args(args)  

    def test_xml_1(self):
        # Add only mandatory parameter
        args = self.args[:]
        argsDict = parse.parse_args(args)
        self.assertFalse(argsDict['xml'])

        file_name = "test.xml"
        args.extend(['-x', file_name])
        argsDict = parse.parse_args(args)
        self.assertEqual(argsDict['xml'],file_name)

        #Clear the last two elemenets from the list
        args[-2:] = []
        args.extend(['--xml', file_name])
        argsDict = parse.parse_args(args)
        self.assertEqual(argsDict['xml'],file_name)
    
    def test_user_1(self):
        # Add only mandatory parameter
        args = self.args[:]
        # Remove the mandatory parameter --user , which is added by default in self.args
        TestSequenceFunctions.removeOptionalArgument(args,'--user')
        with self.assertRaises(BaseException):
            parse.parse_args(args)

        name = 'python'
        args.extend(['-u', name])
        argsDict = parse.parse_args(args)
        self.assertEqual(argsDict['user'],name)

        #Test another format ie --user
        TestSequenceFunctions.removeOptionalArgument(args,'-u')
        args.extend(['--user', name])
        argsDict = parse.parse_args(args)
        self.assertEqual(argsDict['user'],name)

if __name__ == '__main__':
    unittest.main()