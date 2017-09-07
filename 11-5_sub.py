import zmq
import re
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))
topics = ['']
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
# while True:
#     cat_bytes, hat_bytes = sub.recv_multipart()
#     cat = cat_bytes.decode('utf-8')
#     hat = hat_bytes.decode('utf-8')

#     print('Subscribe: %s wears a %s' % (cat, hat))

string = sub.recv_string()
splt = re.split(' ', string)
five_letters = re.findall('.?.?.?.?.?',string)
print(splt)

vewol_list = []
five = []
for word in splt:
    if word[0] in 'aeiou':
        # print(word)
        vewol_list.append(word)
    if word in re.findall(r'\b[A-Za-z]{5}\b',word):
        five.append(word)


print(vewol_list)
print(five)
