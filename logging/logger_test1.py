
# Instead of print to log something use python powerfull logging module

# Load the module
import logging

#basicConfig help us describe log level , log format , log file name
# set file name , file mode append and show only INFO, WARNING, ERROR or CRITICAL message not DEBUGed ones.
# if no any basicConfig described then we will get all things on console not log file.
#logging.basicConfig(filename="logfolder/myfirst.log",level="INFO")

# set file name , file mode write
logging.basicConfig(filename="logfolder/mysecond.log",filemode="w",level="DEBUG")

logging.info("Info message")
logging.debug("Debug message")
logging.error("Error message")