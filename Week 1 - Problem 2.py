# Problem 2
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.
#
# Write a program that prints the number of times the string 'bob' occurs in s.
# For example, if s = 'azcbobobegghakl', then your program should print

v_count = 0
for i in range(2, len(s)):
    if str(s[i-2] + s[i-1] + s[i]) == 'bob':
        v_count += 1
print('Number of times bob occurs is: ' + str(v_count))
