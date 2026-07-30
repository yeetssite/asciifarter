from fartlib import fartrelay, getfart
from time import sleep

print('ASCIIFARTER ART DISPLAY TEST')
print('#=TEST NUM. 1: RELAY=#######')
print('RANDOM ART TEST:')
print('Local Art:')
fart = fartrelay.random_art()
print(fart.get_name())
print(fart.get_art())
sleep(2.5)
print('Remote Art:')
try:
    fart = getfart.random_art()
    print(fart.name)
    print(fart.text)
except Exception as E:
    print('Not Available:\n'+str(E))

input('Press <ENTER> to Continue...')

print('[1A[2KNEWEST ART TEST:')
print('Local Art:')
fart = fartrelay.newest_art()
print(fart.get_name())
print(fart.get_art())
sleep(2.5)
print('Remote Art:')
try:
    fart = getfart.newest_art()
    print(fart.name)
    print(fart.text)
except Exception as E:
    print('Not Available:\n'+str(E))

input('Press <ENTER> to Continue...')

print("[1A[2KART FINDER TEST:")
sleep(0.5)
print("* Using 'DuTCh' as the Search Query...")
sleep(2)
print("Local Art:")
fart = fartrelay.find('DuTCh')
print(fart.get_name())
print(fart.get_art())
sleep(2.5)
print('Remote Art:')
try:
    fart = getfart.find_art('DuTCh')
    print(fart.name)
    print(fart.text)
except Exception as E:
    print('Not Available:\n'+str(E))

input('Press <ENTER> to Complete.')
print('[A[2K', '[A')

