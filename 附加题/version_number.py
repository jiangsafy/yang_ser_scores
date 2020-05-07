v1 = input().split('.')
v2 = input().split('.')
v1 = [int(s) for s in v1]
v2 = [int(s) for s in v2]
index_v = 0
while True:
    if v1 == v2:
        print(0)
        break
    if v1[index_v] > v2[index_v]:
        print(1)
        break
    if v1[index_v] < v2[index_v]:
        print(-1)
        break
    index_v += 1

