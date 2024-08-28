try:
    a = int(input("Hey, Enter a number: "))

except ValueError as v:
    print("\nHeyy,")
    print(v)

except Exception as e:
    print(e)

else:
    print(f"\n{a}\nThis is the number")

print("\nThank YOU!!\n\n")