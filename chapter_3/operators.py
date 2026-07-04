# -----------------------------
# Python Operators Example
# -----------------------------

a = 10
b = 3

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\nLogical Operators")
x = True
y = False
print("x and y :", x and y)
print("x or y :", x or y)
print("not x :", not x)

print("\nAssignment Operators")
c = 5
print("Initial value:", c)

c += 2
print("c += 2 :", c)

c -= 1
print("c -= 1 :", c)

c *= 3
print("c *= 3 :", c)

c /= 2
print("c /= 2 :", c)


# NOTE
# Identity Operators
# Membership Operators
# Bitwise Operators, will be tought letar in the course.

# This code copy pasted from the LLMs.
print("\nIdentity Operators")
p = [1, 2, 3]
q = p
r = [1, 2, 3]

print("p is q :", p is q)
print("p is r :", p is r)
print("p is not r :", p is not r)

print("\nMembership Operators")
numbers = [10, 20, 30, 40]

print("20 in numbers :", 20 in numbers)
print("5 in numbers :", 5 in numbers)
print("5 not in numbers :", 5 not in numbers)

print("\nBitwise Operators")
print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)
