import re

string = 'qwerty jkhsdfi kkd fvkjk 123-78 uef 128-60loopiut'
myNum = re.compile(r'\d\d\d-\d\d')
mo = myNum.search(string)
print(mo.group())

mo1 = myNum.findall(string)
print(mo1)

string2 = 'Welcome ladies and gentleman today 123-456-7890 and everyone here'
myNum2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
moa = myNum2.search(string2)
print(moa.group())
print(moa.group(0))
print(moa.group(1))
print(moa.group(2))

string3 = 'My phone number is (701) 324-8172 and my name is Ajay!'
myNum3 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mob = myNum3.search(string3)
print(mob.group(0))
print(mob.group(1))
print(mob.group(2))
print(mob.group())

string4 = '''
        We four. Ajay, Laxman, Gunnu, Binnu are closest friends! 
'''
friends = re.compile(r'Ajay|Binnu')
moc = friends.search(string4)
print(moc.group())

string5 = 'We are as Laxmajay, Binnajay and Gunnajay'
we = re.compile(r'(Laxm|Binn|Gunn)ajay')
mod = we.search(string5)
print(mod.group())

string6 = 'Iam a fan of flash woman'
flash = re.compile(r'flash (wo)?man')
moe = flash.search(string6)
print(moe.group())

string7 = 'My phone number is 91-123-456-7890'
phone = re.compile(r'(\d\d-)?\d\d\d-\d\d\d-\d\d\d\d')
mof = phone.search(string7)
print(mof.group())

##########################

jreg = re.compile(r'A(j)*ay')
print(jreg.search('Ajay').group())
print(jreg.search('Aay').group())
print(jreg.search('Ajjjjjay').group())

jreg2 = re.compile(r'A(j)+ay')
print(jreg2.search('Ajay').group())
#print(jreg2.search('Aay').group())
print(jreg2.search('Ajjjjjay').group())

string8 = 'My new phone number is 9876543210'
newreg = re.compile(r'\d{10}')
print(newreg.search(string8).group())

haRegex = re.compile(r'(Ha){3,5}')
print(haRegex.search('HaHaHaHaHaHa').group())

greedyhaRegex = re.compile(r'(Ha){3,5}')
nongreedyhaRegex = re.compile(r'(Ha){3,5}?')
print(greedyhaRegex.search('HaHaHaHaHaHa').group())
print(nongreedyhaRegex.search('HaHaHaHaHaHa').group())

xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 23 pipers, 8 lords, 17 ladies, 6 geese 5 rings'))

vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('This is a baby giraffe and Awesome Ajay'))

consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('This is a baby giraffe and Awesome Ajay'))

#^-begins with
#$-ends with
#.-anything except \n

atreg = re.compile(r'.at')
print(atreg.findall('The 8thCat ate rat2, but the 1stbat2 ate 2ndbat1'))
