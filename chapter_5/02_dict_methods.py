d = {} # this is a empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Ankush"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Harry": 99, "Renuka": 100});
# print(marks)

# print(marks.get("Shivika"));
print(marks.get("Harry2")); # => None
# print(marks["Harry2"]); # => error

marks.popitem();
marks.pop("Shubham");
print(marks);