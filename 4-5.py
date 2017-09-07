word = range(10)
letter_counts ={letter:letter*letter  for letter in set(word)}
print(letter_counts)

word = range(10)
letter_cousnt ={letter for letter in set(word) if letter % 2 ==0}

print(letter_counts)