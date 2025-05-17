count_even = 0
for i in range(5):
    if i % 2 == 0:
        count_even += 1
print(f"in 'range(5)' are {count_even} even numbers.")

count_even = 0
for i in range(10):
    if i % 2 == 0:
        count_even += 1
print(f"in 'range(10)' are {count_even} even numbers.")

count_even = 0
for i in range(2, 9, 3):
    if i % 2 == 0:
        count_even += 1
print(f"in 'range(2, 9, 3)' are {count_even} even numbers.")

count_even = 0
for i in range(-4, 6, 2):
    if i % 2 == 0:
        count_even += 1
print(f"in 'range(-4, 6, 2)' are {count_even} even numbers.")

count_even = 0
for i in range(5, 6):
    if i % 2 == 0:
        count_even += 1
print(f"in 'range(5, 6)' are {count_even} even numbers.")
