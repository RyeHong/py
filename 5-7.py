# Make a defaultdict called dict_of_lists and pass it the argument list. Make
# the list dict_of_lists['a'] and append the value 'something for a' to it in one
# assignment. Print dict_of_lists['a'].


from collections import defaultdict
# dict_of_lists= {}
dict_of_lists = defaultdict(list)
dict_of_lists['a'] = 'something for a'
# dict_of_lists = defaultdict(int)
print(dict_of_lists['a'])