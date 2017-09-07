import zmq
import re
host = '127.0.0.1'
port = 6788
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s' % (host, port))
# topics = []
#
# for topic in topics:
#     sub.setsockopt(zmq.SUBSCRIBE, topic.encode('utf-8'))
list = []
# while True:
    # cat_bytes = sub.recv_pyobj('cats')
    # hat_bytes = sub.recv_pyobj('hats')
    #
    # cat_bytes = sub.recv_unicode('cats')

cat_bytes = sub.recv_string()
noSpaceWord = cat_bytes.split(' ')

list = re.findall('.?.?.?.?.?',cat_bytes)
vewol_list = []
for word in noSpaceWord:
    if word[0] in 'aeiou':
        print(word)
        vewol_list.append(word)
print(list )
print('aeiou is %s,5 letters word is %s'% (vewol_list, list))

    # cat = cat_bytes.decode('utf-8')
    # # hat = hat_bytes.decode('utf-8')
    # for a in cat:
    #     list.append(re.findall('.?.?.?.?.?',a))

    # cat1 = re.findall('.?.?.?.?.?',cat_bytes)
        # hat1 = re.findall(r'\b[aeiouAEIOU][A-Za-z].*\b',str(hat))

    # print('Subscribe: %s ' % 1)

    # print('Subscribe: %s wears a %s' % (cat1, hat1))

