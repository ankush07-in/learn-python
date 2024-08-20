'''
For n = 6

*
**
***
****
*****
******

'''


n = int(input("Enter the number: "));

for i in range(1, n+1):
    print("*" * i, end="");
    print("");

print("END");