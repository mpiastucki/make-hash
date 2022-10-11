import os
import hashlib
import sys

def main(args):
    os.chdir(args[1])
    folderItems = os.listdir()
    files = []

    for item in folderItems:
        if os.path.isfile("./"+item) == True:
            files.append(item)
    
    for file in files:
        hash = haslib.sha256()
        f = open("./"+file+"_checksum.txt", "w")

        hash.update("./"+file)
        f.write(hash.hexdigest())
        f.close()
    return

if __name__ == "__main__":
    main(sys.argv)

