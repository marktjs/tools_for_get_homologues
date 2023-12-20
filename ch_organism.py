#this python script can go through all the .gbk and .gbff files in the same directory and replace the /organism="xxx" to /organism="organism_id"
#usage "python ch_organism.py organism_id", organism_id allows white spaces in it

import os
import sys
import re

# Get the organism_id from the command line arguments
organism_id = ' 'join(sys.argv[1:]) #can contain space

# Iterate over all files in the current directory
for filename in os.listdir('.'):
    # Check if the file has a .gbk or .gbff extension
    if filename.endswith('.gbk') or filename.endswith('.gbff'):
        # Read the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Replace the /organism line
        for i, line in enumerate(lines):
            if '/organism=' in line:
                lines[i] = re.sub(r'/organism=".*"', '/organism="{}"'.format(organism_id), line)

        # Write the file
        with open(filename, 'w') as file:
            file.writelines(lines)
