# Read the text file today.txt into the string today_string.
with open('today.txt','rt') as fread:
    today_string = fread.read()
    print(today_string)
