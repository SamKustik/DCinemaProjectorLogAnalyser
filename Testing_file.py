# Log analyser for some digital cinema projectors
# ver.0.00.00.11
# written by Samvel

from typing import Set

print('Hello, my friend! I\'m lazy  application, so put the unpacked logs into application\'s path')
logfile = open('ProjectorLog.txt', 'r')  # opening of standard ProjectorLog file
logfilecontent = logfile.read()
print('But now I\'m gonna count the number of errors')
errorcount = 0  # overall number of errors in logs
charcount = 0
errnum = ""
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
    for line in logfile:
        for c in line:
            if logfilecontent[charcount:charcount+3] == 'err':
                print(line)
            charcount += 1
else:
    print('OK, so we are closing the file.')
logfile.close()


# new function that will find some keywords in parameters file to reveal all the projector info

def wordfinder2(text, keyword):
    start_position = text.find(keyword)
    start_quote = text.find('"', start_position) + 1
    stop_quote = text.find('"', start_quote)
    parameter = text[start_quote:stop_quote]
    return parameter


# next few lines of code are defining several parameters of the projector
# keywords and numeric values for these keywords are ALWAYS the same
# because parameters file has always the same structure
parameters = open('Parameters.txt', 'r')  # opening of standard Parameters file
parameterscontent = parameters.read()

print("Your projector runtime is " + wordfinder2(parameterscontent, 'Projector runtime'))
print("Your projector model is " + wordfinder2(parameterscontent, 'Identifier'))
print("Your projector serial number is " + wordfinder2(parameterscontent, 'serial_number'))
print("Your projector lamp runtime is " + wordfinder2(parameterscontent, 'Lamp runtime'))
print("Your projector lens type is " + wordfinder2(parameterscontent, 'Lens description'))
print("Your projector lens home and return function status: " + wordfinder2(parameterscontent, "Lens_homing_history status"))

if wordfinder2(parameterscontent, 'Identifier')[0:3] == "DPC" or wordfinder2(parameterscontent, 'Identifier')[0:3] == "CMC":
    print("Your projectormake is Cinemeccanica")
elif wordfinder2(parameterscontent, 'Identifier')[0:3] == "DP2" or wordfinder2(parameterscontent, 'Identifier')[0:3] == "DP4":
    print("Your projectormake is Barco")
elif wordfinder2(parameterscontent, 'Identifier')[0:3] == "DCP":
    print("Your projectormake is Kinoton")

parameters.close()

print('\nAnd now we will check cinema front end status...\n')

CinemaFrontEndFile = open('CinemaFrontEndStatus.txt', 'r')

for line in CinemaFrontEndFile:
    print(line)
CinemaFrontEndFile.close()

print('The logfile was successfully opened and closed.')
