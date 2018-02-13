def multiply(arr,num):
    i=0
    while i<len(arr):
        arr[i]=arr[i]*num
        i+=1
    return arr

print (multiply([2,4,10,16],5))
