# only for importing whitelist txt file into Pihole 
# not using Docker

# make sure whitelist-nocomments.txt is in same folder as this py file
# Make sure there are no comments in whitelist file
# Make sure lines dont start with * or . characters
# adobe.com 
# not .adobe.com
# not *.adobe.com

import subprocess
whitelist_file='whitelist-nocomments.txt'

with open(whitelist_file) as whitelist:
  for line in whitelist:
    subprocess.run(["pihole", "-w", line])