'''
def rem(l, word):
    for item in l:
        l.remove(word)
        return l

'''


def rem(l, word):
    n = [];
    for item in l:
        if not(item == word):
            n.append(item.strip(word));
    return n;

l = ["Harry", "Rohan", "Shubham", "an"];

print(l);
print(rem(l, "an"));