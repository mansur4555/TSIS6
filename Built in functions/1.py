x = list(input())
cnt = 1
for i in x:
    if i.isdigit():
        cnt = int(i) * cnt
        

print(cnt)

#BuiltInFunc: list(), isdigit()