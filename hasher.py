import os
import hashlib
import sys

workingdir = os.getcwd() #replace this in your code

def shahash(filepath, blocksize=16*1024*1024): #don't read all of a huge file
    sha1 = hashlib.sha1()
    f = open(filepath, 'rb')
    try:
        sha1.update(f.read(blocksize))
    finally:
        f.close()
    return sha1.hexdigest()

hashoutput = ""

for file in os.listdir(workingdir):
    if os.path.isdir(os.path.join(workingdir, file)):
        pass #exclude folders
    elif file.endswith(".cksum") and file.startswith("sha1"):
        pass #exclude already generated files
    else:
        result = shahash(os.path.join(workingdir, file), 16*1024*1024)
        hashoutput+=str(result)
        hashoutput+=" "
        hashoutput+=str(file)
        hashoutput+=" \n"

target = open(os.path.join(workingdir, 'sha1.cksum'), 'w')
target.write(hashoutput)
target.close()
