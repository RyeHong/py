import subprocess
# Parse the date from today_string
# ret = subprocess.getoutput('date')
with open('today.txt','rt') as fread:
    today_string = fread.read()
    # today_string.format('dd-mm-yyyy')
    print(today_string)