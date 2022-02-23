# Open File in Read Mode
file_1 = open('result.csv', 'r')
file_2 = open('correction.csv', 'r')

print("Comparing files ", " @ " + 'file1.txt', " # " + 'file2.txt', sep='\n')

file_1_line = file_1.readline()
file_2_line = file_2.readline()

# Use as a Counter
line_no = 1
note = 0

print()

while file_1_line != '' or file_2_line != '':

    with open('correction.csv') as file1:
        with open('result.csv') as file2:
            same = set(file1).intersection(file2)
            note +=1
            
    
    # Read the next line from the file
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()

file_1.close()
file_2.close()

# it considers the  lines of two files so i divides by 2
note = int(note/2)

print(f"the student's mark is {note} sur 20")
print('\n')

print("Common Lines in Both Files")
for line in same:
    print(line, end='')

print('\n')
print("Difference Lines in Both Files")

while file_1_line != '' or file_2_line != '':
    # Removing whitespaces
    file_1_line = file_1_line.rstrip()
    file_2_line = file_2_line.rstrip()

    # Compare the lines from both file
    if file_1_line != file_2_line:
        
        # otherwise output the line on file1 and use @ sign
        if file_1_line == '':
            print("@", "Line-%d" % line_no, file_1_line)
        else:
            print("@-", "Line-%d" % line_no, file_1_line)
            
        # otherwise output the line on file2 and use # sign
        if file_2_line == '':
            print("#", "Line-%d" % line_no, file_2_line)
        else:
            print("#+", "Line-%d" % line_no, file_2_line)

        # Print a empty line
        print()
        
    # Read the next line from the file
    file_1_line = file_1.readline()
    file_2_line = file_2.readline()

    line_no += 1

file_1.close()
file_2.close()
