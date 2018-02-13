#New list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
front= x[:len(x)/2]
back= x[len(x)/2:]
back.insert(0,front)
print back
