with open("old.txt") as f:
    content = f.read();

with open("renamed_by_python.txt", "w") as f:
    f.write(content);

# with open("old.txt", "w") as f:
#     f.write("I am old text");