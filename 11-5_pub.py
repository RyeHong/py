import zmq
import time
import re
host = '*'
port = 6789
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
time.sleep(1)

# for msg in range(10):
#     cat = random.choice(cats)
#     cat_bytes = cat.encode('utf-8')
#     hat = random.choice(hats)
#     hat_bytes = hat.encode('utf-8')
#     print('Publish: %s wears a %s' % (cat, hat))
#     pub.send_multipart([cat_bytes, hat_bytes])
splt = poem.split(' ')
print(splt)
pub.send_string(poem)