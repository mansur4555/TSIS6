s = str(input())

cntU = 0
cntL = 0
for i in s:
    if i.isupper():
        cntU = cntU + 1
    elif i.islower() and not i.isdigit(): 
        cntL = cntL + 1

print("Upper letters:", cntU,"\n" "Lower letters:", cntL)

#BuiltInFunctions: str(), isupper(), islower(), isdigit()