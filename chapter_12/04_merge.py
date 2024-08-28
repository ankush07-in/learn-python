# Dictionary merge & update operators

# New operators | and | = allow for merging and updating dictionaries

dict1 = {
    'a': 1,
    'b': 2
}

dict2 = {
    'b': 3,
    'c': 4
}

merged = dict1 | dict2

print(merged)

'''
You can now use multiple context managers in a single line with statement more cleanly using the praenthesised context manager


with (
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    # Process files

    
'''