import os;

directory_path = '/mine/python/test/chapter_1';

contents = os.listdir(directory_path);

for item in contents:
    print(item);