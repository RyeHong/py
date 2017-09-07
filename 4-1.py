guess_me = 7

content = int(input('guess_me'))

if content < guess_me:
    print('too low')
elif content > guess_me:
    print('too high')
elif content == guess_me:
    print('just right')
