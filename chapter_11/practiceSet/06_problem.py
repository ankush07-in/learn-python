# Write __str__() method to print the vector as follows: [7i + 8j + 10k] Assume vector of dimension 3 for this problem

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k"
    
# Test the implementation
v1 = Vector(3, 2, 7)
v2 = Vector(4, 6, 3)


print(v1 + v2) # Output: 7i + 8j + 10k
print(v1 * v2) # Output: 45



...