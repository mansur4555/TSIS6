import string

for letter in string.ascii_uppercase:
    fd = open(letter + ".txt", 'w')
    fd.close()
