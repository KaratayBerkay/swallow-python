letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
# now remove them
letters[2:5] = []
letters
# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
