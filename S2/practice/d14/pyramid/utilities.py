# Utilities

import logging


logger = logging.getLogger("SimpleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)



