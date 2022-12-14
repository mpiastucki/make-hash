import os
import hashlib
import sys

def main(args):

    os.chdir(args[1])

    files = getdirfiles()
    
    for file in files:
        hash = hashlib.sha256()
        f = open("./"+file+"_checksum.txt", "w")
        b = open(file, 'rb')

        hash.update(b.read())
        f.write(hash.hexdigest())
        f.close()
        b.close()
    return

def getdirfiles():
    folderItems = os.listdir()
    files = []

    for item in folderItems:
        if os.path.isfile("./"+item) == True:
            files.append(item)
            
    return files

if __name__ == "__main__":
    main(sys.argv)

