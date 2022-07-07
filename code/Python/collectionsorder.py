from collections import*;
j = int(input());
h = OrderedDict();
for i in range(j):
    item = input().split()
    itemPrice = int(item[-1])
    itemName = " ".join(item[:-1])
    if(h.get(itemName)):
        h[itemName] += itemPrice
    else:
        h[itemName] = itemPrice
for i in h.keys():
    print(i, h[i])