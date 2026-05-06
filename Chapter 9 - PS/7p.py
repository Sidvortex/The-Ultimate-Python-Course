with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:

    if("python" in line):
        print(f"The word python is present in the paragraph on line number {lineno}")
        break
        lineno =+1

    else:
        print("The word is not present in the paragraph")
