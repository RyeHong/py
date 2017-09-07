import re
import zmq
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))
topics = [r'?.?.?.?.?']
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
while True:
    b_bytes = sub.recv_unicode()

    # b = b_bytes.decode('utf-8')
    print(b_bytes)
    print('Subscribe: %s ' % b_bytes )
    # print(b)