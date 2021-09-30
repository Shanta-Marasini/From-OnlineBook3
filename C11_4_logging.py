import logging
logging.basicConfig(filename='logging_fact.txt', level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

#disable log messages
# logging.disable(logging.CRITICAL)

#using logging to see what goes wrong where
logging.debug('start of the program')
print('hello World')
def factorial(n):
    logging.debug('Start of factorial ' + str(n))
    total = 1
    for i in range(1,n+1):
        total *= i
        logging.debug(f'i is {i},total is {total}')
    logging.debug('End of factorial ' + str(n))
    return total

print(factorial(5))
logging.debug('end of the program')
print('How are you')
#disable log messages
logging.disable(logging.CRITICAL)