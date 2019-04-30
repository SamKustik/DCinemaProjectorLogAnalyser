# Log analyser for some digital cinema projectors
# ver.0.00.00.08
# written by Samvel

from typing import Set

print('Hello, my friend! I\'m lazy  application, so put the unpacked logs into application\'s path')
logfile = open('ProjectorLog.txt', 'r')  # opening of standard ProjectorLog file
logfilecontent = logfile.read()
print('But now I\'m gonna count the number of errors')
errorcount = 0  # overall number of errors in logs
charcount = 0
errnum_list = []  # dictionary with all the errors
# in this loop we will find all the errors
for line in open('ProjectorLog.txt', 'r'):
    for c in line:
        if logfilecontent[charcount] == 'e':
            if logfilecontent[charcount+1] == 'r':
                if logfilecontent[charcount+2] == 'r':
                    errorcount += 1
        # this statement will find all the error numbers
        if logfilecontent[charcount] == '#' and logfilecontent[charcount+1] == '5':
            print(line)
            errnum = logfilecontent[charcount + 1:charcount + 5]
            errnum_list.append(errnum)
        charcount += 1
# transforming errnum_list to a set to delete all the repeating errors
errnum_list = set(errnum_list)
# and, finally, we are sorting all the error numbers in ascending error
errnum_list = sorted(errnum_list)
print('The last error in your projector is ' + str(errnum))
print('Full list of error\'s indexes is printed below:' + str(errnum_list))
print('In this file we have ' + str(errorcount) + ' errors')
print('But we printed only REAL errors')
print('If you want - we will display ALL the errors')
charcount = 0
choosed = input('print \'y\' or \'n\': ')
if choosed == 'y':
    for line in open('ProjectorLog.txt', 'r'):
        for c in line:
            if logfilecontent[charcount] == 'e':
                if logfilecontent[charcount+1] == 'r':
                    if logfilecontent[charcount+2] == 'r':
                        print(line)
            charcount += 1
else:
    print('OK, so we are closing the file.')
logfile.close()
print('The logfile was successfully opened and closed.')


