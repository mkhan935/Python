''' I wanted to learn how to log error and do testing, found a video on Youtube
 https://www.youtube.com/watch?v=-ARI4Cz-awo, this is his work, I just followed
 along. '''
import logging
# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.txt',level=logging.DEBUG,
                format='%(asctime)s:%(levelname)s:%(message)s')
def add(x,y):
    ''' Just a simple add func '''
    return x + y

def subtract(x,y):
    ''' Just a sub func '''
    return x - y

def mult(x,y):
    ''' Just a simple multiply func '''
    return x * y

def div(x,y):
    ''' Just a simple divide func '''
    return x / y

num_1 = 12
num_2 = 2

add_result = add(num_1,num_2)
logging.debug('Add: {} + {} = {}'.format(num_1,num_2,add_result))

sub_result = subtract(num_1,num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1,num_2,sub_result))

mul_result = mult(num_1,num_2)
logging.debug('Multiply: {} * {} = {}'.format(num_1,num_2,mul_result))

div_result = div(num_1,num_2)
logging.debug('Divide: {} / {} = {}'.format(num_1,num_2,div_result))
