# only for importing whitelist txt file into Pihole 
# if Pihole is running as a Docker container

# make sure whitelist-nocomments.txt is in same folder as this py file
# Make sure there are no comments in whitelist file
# Make sure lines dont start with * or . characters
# adobe.com 
# not .adobe.com
# not *.adobe.com
import subprocess

whitelist_file='regex-nocomments.txt'
container="cccefea9fcca" # replace with your Pihole's container ID 

with open(whitelist_file) as whitelist:
  for line in whitelist:
    subprocess.run(["docker", "exec", "-it", container, "pihole", "-w", line])