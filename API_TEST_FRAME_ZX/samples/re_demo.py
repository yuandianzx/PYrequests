import re

pattern = re.compile(r'hello,(.+?)!')
str = 'hello,world!abc'
value_findall = re.findall(pattern, str)
print(value_findall)

value_split = re.split('\W', str)
print(value_split)

value_search = re.search(pattern, str)
print(value_search.string)

# pattern = re.compile(r'\${\w+}')
# value_findall = re.findall('\${\w+}','{"access_token":${token}}')



# print(value_findall)


# print('\\t')
