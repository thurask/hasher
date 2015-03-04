import os
import hashlib
import sys

def main(arg1=os.getcwd()):
    workingdir = arg1

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
            pass
        elif file.endswith(".cksum") and file.startswith("sha1"):
            pass
        else:
            result = hash(os.path.join(workingdir, file))
            hashoutput+=str(result)
            hashoutput+=" "
            hashoutput+=str(file)
            hashoutput+=" \n"

    target = open(os.path.join(workingdir, 'sha1.cksum'), 'w')
    target.write(hashoutput)
    target.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        pass
