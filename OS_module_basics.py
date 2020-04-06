import os

#print(dir(os))

print(os.getcwd())

os.chdir('/Users/ajay')

print(os.getcwd())

#print(os.listdir())

os.chdir('/Users/ajay/Regular Python')

os.mkdir('chkOS0')

os.makedirs('chkOS7/chksubFolder')

print(os.listdir())

os.rmdir('chkOS0')

os.removedirs('chkOS7/chksubFolder')

os.rename('testOS.txt','demoOS.txt')

os.rename('demoOS.txt','testOS.txt')

print(os.listdir())

print('\n\n #################################################### \n\n')

print(os.stat('testOS.txt'))

print(os.stat('testOS.txt').st_mtime)

from datetime import datetime

mod_time = os.stat('testOS.txt').st_mtime       #returns modified time

print(datetime.fromtimestamp(mod_time))         #converts mod_time to readable form



##for dirpath, dirnames, filenames in os.walk(os.getcwd()):
##    print('Current path: ', dirpath)
##    print('Directories:', dirnames)
##    print('Files:', filenames)
##    print()
    
print(os.environ.get('HOME'))

filepath = os.path.join(os.environ.get('HOME'), 'test.txt')

print(filepath)


print(os.path.basename('/user/tmp/ajay.txt'))

print(os.path.dirname('/user/tmp/ajay.txt'))

print(os.path.split('/user/tmp/ajay.txt'))

print(os.path.exists('/user/tmp/ajay.txt'))

print(os.path.isdir('/user/tmp/ajay.txt'))

print(os.path.isfile('/user/tmp/ajay.txt'))

print(os.path.splitext('/user/tmp/ajay.txt'))

