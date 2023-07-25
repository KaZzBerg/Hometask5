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
