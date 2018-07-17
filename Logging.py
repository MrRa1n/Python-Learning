# Logging is used for tracking events in software
# It can be configured to disable output or save to a file
import logging

# Print a log message to the console
logging.warning("This is a warning!")

# We can easily output to a file
logging.basicConfig(filename="program.log", level=logging.DEBUG)
logging.warning("Here is an example message...")
logging.warning("Another one!")
