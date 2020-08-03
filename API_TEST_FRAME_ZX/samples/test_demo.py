import ast
import jsonpath
import re
#
# d = '{"access_token":"35_IUABcgKoGmb3PtZe3Ns05oQedDMSYRiAAAGMF","expires_in":7200}'
# a = re.compile(r'"access_token":"35_IUABcgKoGmb3PtZe3Ns05oQedDMSYRiAAAGMF"')
# print(re.findall(a, d))


# if b is not None:
#     print('1')

# a = 'as'
# b = 'bs'
# print('断言失败！期望结果%s与实际结果%s不符合' % (a,b))
#
# c = [(1,2,3,4),(5,6,7,8),9]
# for (d,e,f,g) in c:
#     print(d)

# value = {'aa' : [1,2,3]}
# value.setdefault('aa' , [1,2])
# print(value.setdefault('aa' , [1,2]).append(4))
# print(value)


a = {1, 2, 3, 4}
print(a)