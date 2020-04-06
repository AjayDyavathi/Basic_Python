import re
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('''The | character is called a pipe. You can use it anywhere you want to match one of many expressions. For example, the regular expression r\'Batman|Tina Fey\' will match either \'Batman\' or \'Tina Fey\'.
When both Batman and Tina Fey occur in the searched string, the first occurrence of matching text will be returned as the Match object. Enter the following into the interactive shell:''')

print(mo1.group())
mo2 = heroRegex.search('blah blah blah Tina Fey and again blah Batman blah')
print(mo2.group()) 

batRegex = re.compile(r'Bat(man|mobile|ajay|women)')
mo = batRegex.search('Batajay lost a wheel...!')
print(mo.group())
print(mo.group(1))
