# Text Formatter (Auto-line breaker)
# por Abliveira

import argparse

parser = argparse.ArgumentParser(description="less script")
parser.add_argument('-file', required=True, help="input file containing text to be formatted")
parser.add_argument('-line', required=True, help="input number for the base character quantity per line")
args = parser.parse_args()
# print('args is: ',args)
input_file = args.file
# print(input_file)
f = open(input_file, 'r')
myline = f.readline()
newstring = ''
linesize = int(args.line)

while myline:
    # print(myline, end = '')
    if len(myline) > linesize:

        n = linesize
        newLine = ''
        
        chunks = myline.split()

        i = 0
        while i < len(chunks): # vai percorrer as linhas

            if len(newLine) <= linesize:
                newLine = newLine + ' ' + chunks[i]
                i = i + 1
            else:
                newstring = newstring + newLine + '\n'
                newLine = ''

        newstring = newstring + newLine + '\n'
        newLine = ''    
    else:
        newstring = newstring + myline

    myline = f.readline()

print('')
print(newstring)
f.close

f2 = open("output.txt", 'w')
f2.write(newstring)