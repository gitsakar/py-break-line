#This program breaks large text file into smaller files

#Look for filename huge.txt and prompt user to enter
#number of lines required per smaller file

while True:
    inp = input('Desired Lines per file: ')
      
    try:
        fh = open('huge.txt')
        req = int(inp)
    except:
        print("File 'huge.txt' missing or invalid line number")
        continue
    break

#Initialize first smaller file that

ind = 1
name = 'Part' + str(ind) + '.txt'
f = open(name, 'w+')

end = req

#If the pointer variable exceeds the requested number of lines per file
#a new file is created and variable 'end' is updated

ptr = 1
for line in fh:
    if ptr > end:
        ind = ind + 1
        name = 'Part' + str(ind) + '.txt'
        f = open(name, 'w+')
        
        end = ptr + req - 1
        
    f.write(line)
    ptr = ptr + 1