import logging # to create the logs

class log_generator_class: # created the class to generate and return logger object

    @staticmethod # without creating the class object
    def log_gen_method(): # method and will return logger
        log_file = logging.FileHandler(".\\Logs\\CredKart.log") # log file
        # 2024-08-08 09:12:24,712 - INFO - test_Signup_002  -  Opening browser
        log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s') # log format
        log_file.setFormatter(log_format) # log file --> log format (applying the format to log file)
        logger = logging.getLogger() # getLogger object
        logger.addHandler(log_file) #  add new log everytime in same log file
        logger.setLevel(logging.INFO) # Level set
        return logger


"""
log level : 
pytest doent have logs as like selenium...it has levels.....of python...coz pytest code is written in python
debug--debugging...checking the code
info----for general information about code...whats going on in test case....steps info..
warning---some unexpected issues but programm runs...browser warnings
error---- wrong code due to which code stops....element not found..failed assertions...browser crash..
critical----system crash,Selenium server not reachable.......user not able to login...very basic functionality not workig...


"""

"""
log types:
1.Driver logs: logs from driver itself..i.e.driver not able to find or locate web element..
2.browser logs: captures logs from the browser console..i.e javascript error and warnnings
3.client logs: logs from the client side...ypir test script....api request made by your testcode to webdriver
4.server logs: logs from server side issues
5.performance logs:browser performance...time taken for.page load time...network requestsetc...



"""