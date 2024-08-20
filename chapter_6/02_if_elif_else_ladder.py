a = int(input("Enter your age: "));

if(a>=18):
    print("You are Adult");
    print("Very Good");

elif(a<0):
    print("You are entering an invalid age");
    print("Please, enter your correct age");

elif(a==0):
    print("You are entering 0 which is not valid\nPlease remember I am not stupid");

else:
    print("You are not Adult");

print("End of Program");