#Sometimes, I noticed that the genbank files I downloaded from the NCBI RefSeq do not specified their strain name,
# ,which becomes a bug in the following get_homologues pipeline processing. 
#This script is used to add an "/strain="strain_id" to the gbk or gbff files in the same directory, 
#the strain_id is coppied from the prefix in gbk and gbff files in the same 
#Therefore, remember to rename each gbk and gbff files using their strainnames before this step.

import os
import re

# Iterate over all files in the current directory
for filename in os.listdir('.'):
    # Check if the file has a .gbk or .gbff extension
    if filename.endswith('.gbk') or filename.endswith('.gbff'):
        # Extract the strain ID from the filename
        strain_id = os.path.splitext(filename)[0]

        # Read the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Check if the /strain line is already in the source section
        if not any('/strain=' in line for line in lines):
            # If not, add it
            for i, line in enumerate(lines):
                # Use a regular expression to match the "source" line
                if re.match(r'\s*source\s+1\.\.[0-9]+', line):
                    lines.insert(i + 1, '                     /strain="{}"\n'.format(strain_id))
                    break

            # Write the file
            with open(filename, 'w') as file:
                file.writelines(lines)
