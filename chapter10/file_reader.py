
file_name = 'pi_digits.txt'
with open(file_name) as f:
    contents = f.read()
    print(contents.strip())

with open(file_name) as f:
    for line in f:
        print(line.rstrip())

with open(file_name) as f:
    lines = f.readlines()

pi_string = ''
for line in lines:
    # print(line.rstrip())
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
