# 1.

# def count_lines(path: str) -> int:
#     count = 0
#     try:
#         with open(path, encoding="utf-8") as f:
#             for line in f:
#                 count += 1
#     except FileNotFoundError:
#         print(f'File {path} is not found')
#         return 0
#     return count

# print(count_lines("notes.txt"))

# 2.

# def sum_even(numbers: list[int]) -> int:
#     return sum(x for x in numbers if x % 2 == 0)  

# print(sum_even([1, 3, 6, 11, 32]))

# 3.

# def word_count_from_path(path):
#     words = {}
#     with open(path, encoding='utf-8') as file:
#         for line in file:
#             parts = line.split()
#             for word in parts:
#                 word = word.strip('.,!?').lower()
#                 if word in words:
#                     words[word] += 1
#                 else:
#                     words[word] = 1
#     return words

# print(word_count_from_path('notes.txt'))
    
# 4.

# def find_max(list1):
#     max_val = list1[0]
#     for val in list1:
#         if val > max_val:
#             max_val = val
#     return max_val

# print(find_max(['2', '-3', '7', '0', '-8']))

#------------------------------------

# def del_repeat(list2: list):
#     result = list()
#     seen = set()
#     for word in list2:
#         if word not in seen:
#             result.append(word)
#             seen.add(word)
#     return result
# print(del_repeat(['a', 'b', 'c', 'c', 'b', 'c', 'a', 'b']))

#-----------------------------------

# def is_palindrome(word: str) -> bool:
#     word = word.lower().replace(' ', '')
#     return word == word[::-1]

# print(is_palindrome("EYe"))