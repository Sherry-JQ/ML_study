#encoding=utf-8
import re
secret_code='sdaewcxxIxxfddsfsddbnhjxxlovexxrewuiygdxxyouxxf'

# #'.'类似占位符
# a='xyz123'
# b=re.findall('y....',a)
# print b

# a='xxxy123'
# b=re.findall('x*',a)
# c=re.findall('x?',a)
# print b,c
d=re.findall('xx(.*?)xx',secret_code)
print d
for each in d:
    print each

f=re.search('xx(.*?)xxfddsfsddbnhjxx(.*?)xx',secret_code).group(2)
print f
f1=re.findall('xx(.*?)xxfddsfsddbnhjxx(.*?)xx',secret_code)
print f1[0][1]
f2=re.findall('xx(.*?)xx',secret_code)
print f2[1]