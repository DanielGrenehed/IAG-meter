#! /usr/bin/python

import sys
from arg_parser import ArgParser
from insuline_injection_logger import IILogger, IIL_Wrapper
from time_provider import get_time

"""
# saving parsering time?

def test_callback(arg):
    print("TestParser : ",str(arg))

def test_arg_parser():
    arguments = ["test", "Hello World"]
    function_map = {"test": (1, test_callback), }
    AP = ArgParser(function_map)
    AP.parse_arguments(arguments)
"""

def startup(arguments):
    #test_arg_parser()

    # check that arguments works.
    print('Number of arguments:', len(arguments), 'arguments.')
    print('Argument list:', str(arguments))
    arguments = arguments[1:] # remove filename argument

    a_parser = ArgParser({})

    i_logger = IIL_Wrapper("*database*", get_time)
    a_parser.append_function_map(i_logger.get_function_map())

    a_parser.parse_arguments(arguments)
    #



startup(sys.argv)
