
def is_palindrom(name):
    
    name = ''.join([i for i in name if i.isalpha()])

    if len(name) % 2 == 0:
        y = int(len(name)/2)
    else: 
        y = int((len(name)-1)/2)


    for x in range(y):
        if name[x] != name[-(x+1)]:
            b = False
        elif name[x] == name[-(x+1)]:
            b = True

    if b == False:
        print('it is not a palindrom')
    elif b == True:
        print('it is a palindrom!')



is_palindrom('Kobyła 44 4 ma mały bok.')
