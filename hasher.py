import os
import hashlib
import sys

workingdir = os.getcwd() #replace this in your code

def hash(filepath):
    sha1 = hashlib.sha1()
    f = open(filepath, 'rb')
    try:
        sha1.update(f.read())
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
        result = hash(os.path.join(workingdir, file))
        hashoutput+=str(result)
        hashoutput+=" "
        hashoutput+=str(file)
        hashoutput+=" \n"

target = open(os.path.join(workingdir, 'sha1.cksum'), 'w')
target.write(hashoutput)
target.close()
