with open ("this.txt", "r") as f:
    content1 = f.read()

with open ("copy.txt", "r") as f:
    content2 = f.read()

    if content1 == content2:
        print ("yes both files are identical")
    else:
        print ("no these both files are not identical")