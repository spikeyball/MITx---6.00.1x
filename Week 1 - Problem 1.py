# Problem 1
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.
#
# Write a program that counts up the number of vowels contained in the string s.
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if
# s = 'azcbobobegghakl', your program should print:

v_count = 0
for char in s:
    if char in 'aeiou':
        v_count += 1
print(v_count)
