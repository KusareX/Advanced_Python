# 1.

def even(numbers: list):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

print(even([2, 4, 8, 9]))

# 2.

def string(row: str):
    words = {}
    parts = row.split()
    for r in parts:
        if r in words:
            words[r] += 1
        else:
            words[r] = 1
    return words
    
print(string('Hello hello'))
# 3.

with open ('notes.txt', encoding='utf-8') as f:
    count = 0
    for line in f:
        count += 1
print(count)
        
# 4.

# [x * 2 for x in range(5)] виведе 0, 2, 4, 6, 8
# основна відмінність кортежа і списку полягає в тому що всі елементи кортежу незмінні (immutable)