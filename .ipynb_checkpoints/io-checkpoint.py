#This module coordinates all input and output
#take as input the map text file and have a routine to
#delete empty spaces as needed and fill the hex appropriately
# as per the list with the coordinates and contents.
#
path = './hexgrid.txt'

hexmap = open(path,'r')
output = hexmap.read().splitlines()
print(output)
for i in range(len(output)):
    print(output[i])


