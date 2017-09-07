import redis
import time
# Write a simulation that pushes different types of chocolates to a Redis list, and Lucy is
# a client doing blocking pops of this list. She needs 0.5 seconds to handle a piece of
# chocolate. Print the time and type of each chocolate as Lucy gets it, and how many
# remain to be handled.
conn = redis.Redis()
print('push is starting')
chocolates = ['A', 'B', 'C', 'D']
tcount = 0.5
temp =chocolates.copy()
for dish in chocolates:
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    time.sleep(0.5)
    temp.remove(dish)
    print('Create Chocolate', dish)
    print('time',tcount)
    tcount += 0.5
    print('Remain Chocolate',temp)
conn.rpush('chocolates', 'quit')
print('push is done')