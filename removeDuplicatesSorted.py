res=[0,0,1,1,1,2,2,3,3,4]
print(res)
i=0
for j in range(1,len(res)):
    if res[j]!=res[i]:
        i+=1
        res[i]=res[j]
print(res)