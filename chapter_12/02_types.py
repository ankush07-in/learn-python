# type definitions in python

n = 5
n : int = 5

name : str = "Lewandoski"

def sum(a: int, b: int) -> int:
    return a+b

k = sum(4, 3)
print(f"00{k}")


# Variable type hint
age: int = 25

# Function type hints
def greeting(name: str)-> str:
    return f"Hello, {name}!"

# Usage
print(greeting("Ankush"))


...