from itertools import permutations

s = [0,5,10,15]
count = 0
x1,x2,x3,x4=0,0,0,0
j,k,l,m=0,0,0,0
for i in s:
  for j in range(i+1):
    for k in range(i+1):
      for l in range(i+1):
        for m in range(i+1):
          if j+k+l+m==i: 
            count+=1

print(count)

count = [[j,k,l,m] for i in s for j in range(i+1) for k in range(i+1) for l in range(i+1) for m in range(i+1) if j+k+l+m==i]
print(len(count))
#print(count)

count = [1 for i in s for j in range(i+1) for k in range(i+1) for l in range(i+1) for m in range(i+1) if j+k+l+m==i]
print(sum(count))
ss=0
perm =[i for ss in s for i in range(ss) for j in range(4)]
print(perm)
perm = permutations([0,0,0,0,1,1,1,1, 2,2,2,2, 3,3,3,3, 4,4,4,4, 5,5,5,5], 4)
for i in list(perm): 
  #print (i)
  #y = input("enter a key:")
  if sum(i) == 5:
    print(i)
    y = input("enter a key at sum:")