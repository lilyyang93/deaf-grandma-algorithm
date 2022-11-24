def deaf_grandma():
    bye = 0
    greeting = input('HEY KID!\n')
    while not greeting:
        greeting = input('WHAT?!\n')
    while greeting:
        if greeting == greeting.upper() and not greeting == 'GOODBYE':
            greeting = input('NO, NOT SINCE 1946!\n')
        elif greeting == greeting.lower():
            greeting = input('SPEAK UP, KID!\n')
        elif greeting == 'GOODBYE' and bye < 1:
            greeting = input('LEAVING SO SOON?\n')
            bye+=1
        elif greeting == 'GOODBYE':
            print('LATER, SKATER!')
            return 0
        while not greeting:
            greeting = input('WHAT?!\n')
deaf_grandma() 