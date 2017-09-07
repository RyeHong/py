import binascii
import struct



word = '47494638396101000100800000000000ffffff21f9' +\
'0401000000002c000000000100010000020144003b'
gif = binascii.unhexlify(word)

width = struct.unpack('>16s', gif[6:22])
height = struct.unpack('>16s',gif[8:24])


print('Valid PNG, width', width, 'height', height)
