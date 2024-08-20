marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (marks1+marks2+marks3)/3;

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You Passed", total_percentage);

else:
    print("You Failed. Try again next year", total_percentage);