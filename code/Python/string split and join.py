def split_and_join(line):
    x = line.split(" ")
    x = "-".join(x)
    return x
line = input()
result = split_and_join(line)
print(result)