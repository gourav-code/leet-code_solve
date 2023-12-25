
l=[3,6,7,11]
h=8
temp=0
k=(sum(l)+h-1)//h
print(f"max element:{max(l)}")
while(k<=max(l)+1):
    temp=0
    for tmp in l:
        temp+=(tmp+k-1)//k
    if(temp==h):
        print(f"yes: k={k}")
        break
    else:
        print(f"k:{k}, temp:{temp}")
    k+=1

#this(brute force) is not best approach we can binary search between 1 and max(l)
