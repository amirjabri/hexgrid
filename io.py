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
def insert_sequence(str1, str2, int):        
	str1_split1 = str1[:int]
	str1_split2 = str1[int:]
	new_string = str1_split1 + str2 + str1_split2
        return new_string

