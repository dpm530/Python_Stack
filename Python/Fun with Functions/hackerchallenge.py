def multiply(arr,num):
    i=0
    while i<len(arr):
        arr[i]=arr[i]*num
        i+=1
    return arr

#print (multiply([2,4,10,16],5))

def layeredmultiples(arr):
    print arr
    answer=[]
    i=0
    while i<len(arr):
        i2=0
        temp=[]
        while i2<(arr[i]):
            temp.append(1)
            i2+=1
        answer.append(temp)
        i+=1
    return answer


print (layeredmultiples(multiply([2,4,5],3)))
