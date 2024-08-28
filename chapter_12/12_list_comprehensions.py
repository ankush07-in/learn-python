myList = [1, 2, 9, 5, 3, 5]

squaredList1 = []

for item in myList:
    squaredList1.append(item*item)


squaredList = [i*i for i in squaredList1]

print(f"The normal list is: {myList}")
print(f"The squared list is: {squaredList}")



...