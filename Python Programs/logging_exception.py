from logging import *

# logging is used to keep the records of errors.
'''some imp formats:  
%(asctime)s - gives current time.
%(message)s - gives the error msg.
%(levelname)s - give type of level ( CRITICAL(50), ERROR(40), WARNING(30), INFO(20), DEBUG(10), NOTSET(0)
%(lineno)d - gives the line no from where the error is written on log file. '''

basicConfig(filename = 'Testlog.log', level = ERROR, format = '%(lineno)d || %(asctime)s || %(message)s')

# logging  import krna hi padega.
# level = ERROR, likha hai to sirf ERROR aur uske uppar wale levels ko consider krega
# like CRITICAL will be accepted but warning, info, debug will be ignored.

# below msgs will be written on log file each time when this program will be called.
error('this is an error')
critical('this is critical')
warning('this is warning')
info('this is info.')
debug('this is debug')
#--------------------------------------------------------------------------------------------

# if user want to write exception on the log file then,
# use logging.Exception('msg') in EXCEPT block.

class user(Exception):   # created for  user defined exception.
    def __init__(self, args):
        self.msg = args
try:
    a = int(input('enter num: '))
    if a < 0:
        raise user('invalid value...plz enter value greater than 0.')
    else:
        print(f'You entered: {a}')
except user as e:
    exception(e)

# ek concept bachta hai.....to create our own logger when we try to import the logger.