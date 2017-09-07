import zmq
import random
import time
import re
host = '*'
port = 6788
ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind('tcp://%s:%s' % (host, port))

poem = "We have seen thee, queen of cheese,\
Lying quietly at your ease,\
Gently fanned by evening breeze,\
Thy fair form no flies dare seize.\
All gaily dressed soon you'll go\
To the great Provincial show,\
To be admired by many a beau\
In the city of Toronto.\
Cows numerous as a swarm of bees,\
Or as the leaves upon the trees,\
It did require to make thee please,\
And stand unrivalled, queen of cheese.\
May you not receive a scar as\
We have heard that Mr. Harris\
Intends to send you off as far as\
The great world's show at Paris.\
Of the youth beware of these,\
For some of them might rudely squeeze\
And bite your cheek, then songs or glees\
We could not sing, oh! queen of cheese.\
We'rt thou suspended from balloon,\
You'd cast a shade even at noon,\
Folks would think it was the moon\
About to fall and crush them soon."
#
# cats = re.findall('.?.?.?.?.?',poem)
# hats = re.findall(r'\b[aeiouAEIOU][A-Za-z].*\b',poem)
time.sleep(1)

cats = poem.split(' ')
hats = poem.split(' ')
# for c in cats:
#     # cat = random.choice(cats)
#     # cat_bytes = c.encode('utf-8')
#     # hat = random.choice(hats)
#     # hat_bytes = h.encode('utf-8')
#     print('Publish: %s ' % c)
#     print('Publish: %s wears a %s' % (c, h))
#     pub.send_multipart([cat_bytes, hat_bytes])

#
# pub.send_pyobj(hats)
# pub.send_pyobj(cats)

pub.send_string(poem)