def find(list,char):
    newlist=[]
    for i in list:
        if char in i:
            newlist.append(i)
    print newlist

find(['hello','world','my','name','is','Anna'],'o')
