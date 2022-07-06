a = int(input())
storage1 = set(input().split());
b = int(input())
storage2 = set(input().split());
storage3 = storage1.union(storage2)
print(len(storage3))