# Author Daniel Amos Grenehed

"""
Handle insuline injection data
    example arguments:
    ->  H 7e
        Humalog, 7 units, now
    ->  L 16e 20.39
        Lantus, 16 units, today 20:39
"""

class IILogger(object):
    """docstring for IILogger.

        Insuline Injection Logger
    """

    def __init__(self, storage): # change arg to storage abstraction
        super(IILogger, self).__init__()
        self.storage = storage

    """
        Store data in storage
    """
    def log_intake(self, ammount, insuline_type, time):
        # store data.
        print("a", str(ammount), " t", insuline_type, " d", time)
        pass


class IIL_Wrapper(object):
    """docstring for IIL_Wrapper.

        wrapper functions for IILogger
    """

    def __init__(self, arg, get_time):
        super(IIL_Wrapper, self).__init__()
        self.logger = IILogger(arg)
        self.get_time = get_time
        self.__construct_function_map()

    """
        Create a alias map for functions
    """
    def __construct_function_map(self):
        self.function_map = {
            "IH": [1, self.log_humalog_now], # IH: Humalog, units (now)
            "Ih": [2, self.log_humalog], # Ih: Humalog, units, time
            "IL": [1, self.log_lantus_now], # IL: Lantus, units (now)
            "Il": [2, self.log_lantus], # Il: Lantus, units, time
        }

    """
        Return the function_map
    """
    def get_function_map(self):
        return self.function_map

    """
        Log insuline injection of type Humalog
    """
    def log_humalog(self, param):
        ammount, time = param
        self.logger.log_intake(int(ammount), "humalog", time)

    """
        Log insuline injection of type Humalog with time set to current time
    """
    def log_humalog_now(self, param):
        ammount, = param
        self.log_humalog([ammount, self.get_time()])

    """
        Log insuline injection of type Lantus
    """
    def log_lantus(self, param):
        ammount, time = param
        self.logger.log_intake(int(ammount), "lantus", time)

    """
        Log insuline injection of type Lantus with time set to current time
    """
    def log_lantus_now(self, param):
        ammount, = param
        self.log_lantus([ammount, self.get_time()])
