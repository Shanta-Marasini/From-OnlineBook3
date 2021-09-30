import traceback
print('Hello my world')

#getting traceback as a string
#traceback.format_exe

try:
    raise Exception('This is an exception ok.')
except:
    errorFile = open('errorFile.txt','w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The error was written successfully.')

