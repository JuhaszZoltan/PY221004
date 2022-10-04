nev = input('Írd be a neved: ')
print(f'Hello {nev}!')
print(f'Milyen szép név az, hogy {nev}!')
print(f'Szerintem már most Beléd vagyok zúgva {nev}! uwu <3')

print(f'Amúgy tudtad, hogy 2+2 az {2 + 2}?')

valasz = input(f'Szeretsz programozni, {nev}? ')
if valasz.lower() in { 'igen', 'ja', 'aha', 'hogyne' }:
    print('Akkor itt jól fogod érezni magad!')
else:
    print('Hát, remélem majd megszereted... :(')

szam = int(input('Hánszor írjam ki a neved? '))
for x in range(szam):
    print(f'{nev}', end=' ')

