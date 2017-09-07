word = range(10)
letter_counts ={letter for letter in set(word) if letter % 2 ==0}

print(letter_counts)