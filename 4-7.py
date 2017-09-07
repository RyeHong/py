# Use a generator comprehension to return the string 'Got ' and a number for the
# numbers in range(10). Iterate through this by using a for loop.

word = range(10)
letter_counts = {letter  for letter in word}
# print(letter_counts)

for letter_count in letter_counts:
    print('Got',letter_count)

