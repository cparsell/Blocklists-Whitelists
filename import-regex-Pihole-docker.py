# only for importing whitelist txt file into Pihole 
# if Pihole is running as a Docker container

# make sure whitelist-nocomments.txt is in same folder as this py file
# Make sure there are no comments in whitelist file
# Make sure lines dont start with * or . characters
# adobe.com 
# not .adobe.com
# not *.adobe.com
import subprocess

regex_file='regex-nocomments.txt'
container="cccefea9fcca" # replace with your Pihole's container ID 

with open(regex_file) as regex:
  for line in regex:
    subprocess.run(["docker", "exec", "-it", container, "pihole", "--regex", line])