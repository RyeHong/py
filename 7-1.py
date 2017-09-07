import unicodedata
mystery = '\U0001f4a9'
value = unicodedata.lookup('\u00a2')

print('value = "%s"' % value)
