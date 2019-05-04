# Log analyser for some digital cinema projectors
# ver.0.00.00.10
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
        if logfilecontent[charcount:charcount+3] == 'err':
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
            if logfilecontent[charcount:charcount+3] == 'err':
                print(line)
            charcount += 1
else:
    print('OK, so we are closing the file.')
logfile.close()


# new function that will find some keywords in parameters file to reveal all the projector info
# I will add some clarity for variables a little bit later
# but believe me - it is working for now
# yes - there is some bugs
# but this is pre-pre-pre-alfa version and at present stage it is working normally
# I'm working on optimization and - SURPRISE - GUI version on Qt
def wordfinder(z, x, q, v, b, n):
    ch = 0
    m = ''
    for u in z:
        if z[ch:ch + q] == x:
            for t in z[ch + v:ch + b]:
                if t != n:
                    m = m + t
                elif t == n:
                    break
        ch += 1
    return(m)


# next few lines of code are defining several parameters of the projector
# keywords and numeric values for these keywords are ALWAYS the same
# because parameters file has always the same structure
parameters = open('Parameters.txt', 'r')  # opening of standard Parameters file
parameterscontent = parameters.read()

print("Your projector runtime is " + wordfinder(parameterscontent, 'Projector runtime', 17, 19, 24, '\"'))

print("Your projector model is " + wordfinder(parameterscontent, 'Identifier', 10, 12, 30, '\"'))

print("Your projector lamp type is " + wordfinder(parameterscontent, 'Lamp runtime', 12, 14, 20, '\"'))

print("Your projector lens type is " + wordfinder(parameterscontent, 'Lens description', 16, 18, 78, '\"'))

print ("Your projector lens home and return function status" + wordfinder(parameterscontent, "Lens_homing_history status", 26, 28, 60, '\"'))

parameters.close()

print('test')

print('The logfile was successfully opened and closed.')
