def goodDay(name, ending):
    print("Good Day, "+name+". "+ending);


goodDay("Ankush", "Thank You");
goodDay("Divya", "How are you??");
goodDay("Rohan", "Hope you are well");
goodDay("Harry", "Welcome!!");


def goodDay(name, ending):
    print(f"Good day, {name}. {ending}");
    return "EXIT"


then = goodDay("Ankush", "Thank You");
print(then);