filename = 'alice.txt'
try:
    with open(filename) as f:
        content = f.read()
except FileNotFoundError:
    pass
    # print("Sorry, the file " + filename + " does not exist.")
