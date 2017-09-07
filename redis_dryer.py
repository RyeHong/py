import redis
import time
conn = redis.Redis()
print('Pop is starting')


while True:
    msg = conn.blpop('chocolates')

    if not msg:
        break
    val = msg[1].decode('utf-8')
    if val == 'quit':
        break
        print('Dried', val)
print('Pops are finished')