def get_odds():
        a = {number for number in range(10) if number % 2 == 0}
        return a


count = 0
for third in get_odds():

    if count == 2:
        print('third',third)
    count += 1


