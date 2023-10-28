""" lec_fileio.py

Companion codes for the lecture on reading and writing files
"""

import os

import toolkit_config as cfg


SRCFILE = os.path.join(cfg.DATADIR, 'qan_prc_2020.csv')
DSTFILE = os.path.join(cfg.DATADIR, 'new_file.txt')

# ----------------------------------------------------------------------------
#   Opening the `SRCFILE` and reading its contents
# ----------------------------------------------------------------------------
# This will open the file located at `SRCFILE` and return a handler (file
# object):
fobj = open(SRCFILE, mode='r')
# We can get the entire content of the file by calling the method `.read()`,
# without parameters:
cnts = fobj.read()

# The variable `cnts` will be a string containing the full contents of the
# file. This will print the first 20 characters:
print(cnts[:20])
# Output:
#  Date,Open,High,Low,C
# Check if the file is closed
print(fobj.closed)  # --> False
# Close the file
fobj.close()
print(fobj.closed)  # --> True