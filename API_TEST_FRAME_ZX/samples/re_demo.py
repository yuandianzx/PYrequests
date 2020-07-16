import re

# pattern = re.compile(r',')
# str = 'hello,world!'
# value_findall = re.findall(pattern, str)
# print(value_findall)
#
# value_split = re.split(pattern, str)
#
# print(value_split)

value_findall = re.findall('\w+','liuyaN1234ab9')
print(value_findall)

# print('\\$')