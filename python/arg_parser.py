"""#! /usr/bin/python"""

"""
function map:
    { "alias": [num_parameters, callback] }
"""


"""
default error logger.
"""
def default_error(arguments):
    print("ERROR:", arguments)

class ArgParser(object):
    """docstring for ArgParser.

        Calls callbacks of function_map when
        parsing_arguments

    """

    def __init__(self, function_map, error_log=None):
        super(ArgParser, self).__init__()
        self.function_map = function_map
        self.__set_logger(error_log)

    def __set_logger(self, error_log):
        if error_log == None:
            error_log = default_error
        self.error_log = error_log

    def append_function_map(self, function_map):
        self.function_map.update(function_map)
        #print("updated function_map: ", str(self.function_map))

    def parse_arguments(self, arguments):
        num_args = len(arguments)

        i = 0
        while i < num_args: # for all arguments
            arg = arguments[i] # current iterations argument
            try:
                num_param, callback = self.function_map.get(arg) # unwrap callback

                if (num_args - i) - num_param >= 0: #if there is enough arguments for the callback parameters
                    next_i = i+1

                    callback_arguments = arguments[next_i : next_i + num_param]

                    callback(callback_arguments) # call the callback and privde arguments for the parameters
                    i += num_param # skip the arguments that were provided for callback parameters.

                else: # not enough arguments to provide for callback parameters
                    self.error_log("Too few arguments given for "+ str(arg))
                pass
            except Exception as e:
                self.error_log("(Argument '"+str(arg)+"') "+str(e)) #something went wrong, print exception

            i += 1 # forward iterator
        pass
