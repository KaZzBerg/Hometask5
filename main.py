import random

NUM_SIZE = 10
numbers = []
for i in range(NUM_SIZE):
    numbers.append(random.randint(-5, 5))
print(numbers)

y = [i for i in numbers if i % 2 == 0]
x = [i for i in numbers if i < 0]
z = [i for i in numbers if i % 2 != 0]

print('Sum of negative numbers:', sum(x))
print('Sum of even Positive numbers:', sum(y))
print('Sum odd numbers:', sum(z))
print(f'Sum of every third number:', sum(numbers[2:15:3]))
print(f'Multiplication of max and min values:', max(numbers) * min(numbers))
try:
    s1 = s2 = 0
    for s1, a in enumerate(numbers):
        if a > 0:
            break
    for s2, a in enumerate(reversed(numbers)):
        if a > 0:
            break
    s = sum(numbers[s1 + 1: -s2 - 1])
    print(f'Sum of numbers between:', {s})
except ValueError as e:
    print(f'Error: {e}')

    print('No positive numbers')

    print('No positive numbers')

print(y)
print(z)
print(x)
h = [i for i in numbers if i > 0]
print(h)
