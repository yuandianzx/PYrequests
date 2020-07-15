import re

pattern = re.compile(r',')
str = 'hello,world!'
value_findall = re.findall(pattern, str)
print(value_findall)

value_split = re.split(pattern, str)

print(value_split)