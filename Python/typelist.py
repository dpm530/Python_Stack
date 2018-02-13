def typelist(list):
    sum=0
    string=""
    i=0
    while i<len(list):
        if type(list[i]) == str:
            string+=list[i]
        elif type(list[i]) ==int:
            sum+=list[i]
        i+=1


    if sum>0 and len(string)>0:
        print "The array you entered is of mixed type."
        print "string:{}".format(string)
        print "sum:{}".format(sum)
    elif sum<1:
        print "The array you entered is of string type."
        print "string:{}".format(string)
    elif len(string)==0:
        print "The array you entered is of integer type."
        print "sum:{}".format(sum)


typelist(['magical unicorns',19,'hello',98.98,'world'])
typelist([2,3,1,7,4,12])
typelist(['magical','unicorns'])
