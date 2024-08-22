with open("this.txt") as f:
    content = f.read();

with open("this_copy2.txt", "w") as f:
    f.write(content);