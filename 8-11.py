import redis
conn = redis.Redis()

conn.hmset('test',{'count':1,'name':'Fester Bestertester'})
print(conn.hmget('test', 'count','name'))



