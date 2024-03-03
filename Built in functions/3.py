t = str(input())

flag = True
leng = len(t)

for i in range(leng // 2):
    if t[i] != t[leng - 1 - i]:
        flag = False
        break

print(flag)

#BuiltInFunctions: str(), range(), len()