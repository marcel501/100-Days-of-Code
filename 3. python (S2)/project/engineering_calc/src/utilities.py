'''
Utility module for python project logging


'''

import logging

logger = logging.getLogger("SimpleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("../debug/app.log")
logger.addHandler(file_handler)



