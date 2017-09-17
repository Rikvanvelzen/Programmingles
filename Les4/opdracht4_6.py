def wijzig(letterlijst):
    lijst[0],lijst[1],lijst[2] = 'd', 'e', 'f'
    #de lijst kan ik eventueel ook legen met del lijst[:] namelijk:
    #del lijst[:]
    #lijst.append('d')
    #lijst.append('e')
    #lijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)
