import os
import hashlib
import sys

def main(arg1=os.getcwd(), arg2=16*1024*1024):
    def hash(filepath):
        sha1 = hashlib.sha1()
        f = open(filepath, 'rb')
        try:
            sha1.update(f.read(arg2))
        finally:
            f.close()
        return sha1.hexdigest()
    hashoutput = ""
    for file in os.listdir(arg1):
        if os.path.isdir(os.path.join(arg1, file)):
            pass
        elif file.endswith(".cksum") and file.startswith("sha1"):
            pass
        else:
            result = hash(os.path.join(arg1, file))
            hashoutput+=str(result)
            hashoutput+=" "
            hashoutput+=str(file)
            hashoutput+=" \n"

    target = open(os.path.join(arg1, 'sha1.cksum'), 'w')
    target.write(hashoutput)
    target.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1], sys.argv[2])
    else:
        pass
