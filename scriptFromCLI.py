#! /usr/bin/env python3

#pw.py - An insecure password locker!

import pyperclip,sys

passwords = {'email': 'Ajay123',
             'facebook': 'AjayAwesome',
             'twitter': 'AsAwesomeAsAjay'}
if len(sys.argv)<2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for {} has been copied to clipboard.'.format(account))
else:
    print('There\'s no password for {}'.format(account))
