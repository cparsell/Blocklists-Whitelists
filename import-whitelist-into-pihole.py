# only for importing whitelist txt file into Pihole 
# not using Docker

import subprocess
whitelist_file='whitelist-nocomments.txt'

with open(whitelist_file) as whitelist:
  for line in whitelist:
    subprocess.run(["pihole", "-w", line])