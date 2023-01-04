import logging
import time

# Make the logger print to stderr as well as log to file
logging.basicConfig(handlers=[
    logging.FileHandler("APRS_log.txt"),
    logging.StreamHandler()
], level=logging.DEBUG,
    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# Should only print in console
print("bruh")

# Should print (append) to file as well
logging.debug("Msg1\nMsg1.5")
logging.debug("Msg2")
logging.debug("Msg3")
logging.debug("Msg4")

# Test joining strings into one log message
logMsgs = ["a", "e", f"i{time.time()}", "o", "u"]
logging.debug("\n".join(logMsgs))
logging.info("er")
logging.debug("\n".join(logMsgs))
