Multiples

for i in range(1,1000):
    if i%3==0:
        print i

for i in range(5,1000000):
    if i%5==0:
        print i

#Sum list
a=[1,2,5,10,255,3]
answer=0
i=0
while i<(len(a)):
    answer+=a[i]
    i+=1

print answer

#Average List
a=[1,2,5,10,255,3]
answer=0
i=0
while i<(len(a)):
    answer+=a[i]
    i+=1

print answer/len(a)
