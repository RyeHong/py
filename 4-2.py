guess_me = 7
start = 1
print('guess_me',guess_me)
while 1 :
    if start < guess_me:
        print('start',start,'too low')
    elif start == guess_me:
        print('found it!',start)
        break
    elif start > guess_me:
        print('oops',start)
        break
    start += 1