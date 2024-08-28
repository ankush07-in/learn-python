
user_name = input("Enter your name: ")
profile = input("Enter your gender/character/profession/profile: ")

a = "{} is a good {}".format(user_name, profile)

score = input("Enter your score: ")
subject = input("Enter your subject: ")

x = score
y = subject

print(a)

new = "In {1} subject you got {0} marks".format(x, y)

print(new)


...