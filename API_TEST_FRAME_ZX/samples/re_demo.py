import re

pattern = re.compile(r',')
str = 'hello,world!'
value_findall = re.findall(pattern, str)
print(value_findall)
#
# value_split = re.split(pattern, str)
#
# print(value_split)

# pattern = re.compile(r'\${\w+}')
# value_findall = re.findall('\${\w+}','{"access_token":${token}}')



# print(value_findall)


# print('\\t')
