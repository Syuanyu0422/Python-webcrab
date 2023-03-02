import re
key='ABC XYZ DEF BCD CDE'

p1=re.compile('X.')
p2=re.compile(r'^A.+Z')
p3=re.compile(r'D\wF.*\S[BCD].+E$')

print(p1.findall(key)[0])
print(p2.findall(key)[0])
print(p3.findall(key)[0])