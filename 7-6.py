# Make a dictionary called response with values for the string keys 'salutation',
# 'name', 'product', 'verbed' (past tense verb), 'room', 'animals', 'amount', 'per
# cent', 'spokesman', and 'job_title'. Print letter with the values from response
response = { 'salutation':'salutation',
             'name':'name',
             'product':'product',
             'verbed':'verbed',
             'room':'room',
             'animals':'animals',
             'amount':'amount',
             'percent':'percent',
             'spokesman':'spokesman',
             'job_title':'job_title'
}

letter = 'Dear ''{0[salutation]} {0[name]}'\
'Thank you for your letter. We are sorry that our {0[product]} {0[verbed]} in your\
{0[room]}. Please note that it should never be used in a {0[room]}, especially\
near any {0[animals]}.\
Send us your receipt and {0[amount]} for shipping and handling. We will send\
you another {0[product]} that, in our tests, is {0[percent]}% less likely to\
have {0[verbed]}.\
Thank you for your support.\
Sincerely,\
{0[spokesman]}\
{0[job_title]}'''
print(letter.format(response))
# Make a dictionary called response with values for the string keys 'salutation',
# 'name', 'product', 'verbed' (past tense verb), 'room', 'animals', 'amount', 'per
# cent', 'spokesman', and 'job_title'. Print letter with the values from response