birthdays = {'Ajay':'Jan 2', 'Laxman':'Sep 3', 'Mom':'Oct 16', 'Binnu':'Sep 10'}

while True:
    name = input('Enter a name: (blank to quit)')
    if name == '':
        break
    else:
        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else: 
            print('Sorry!, I dont have birthday information for ' + name)
            date = input('What\'s their birthday?')
            birthdays[name] = date
            print('Database Updated!')
            
