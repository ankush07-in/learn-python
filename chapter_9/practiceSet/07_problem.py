
with open("log.txt") as f:
    lines = f.readlines();

lineNo = 1;

for line in lines:

    if("python" in line):
        print(f"Yes, python is present in Line no:{lineNo}");
        break;
    lineNo = lineNo + 1;

else:
    print("No pyhton is not present");