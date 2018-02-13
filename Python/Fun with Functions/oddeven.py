def oddeven():
    i=1
    while i<=2000 :
        if i%2==0 :
            print ("Number is {}. This is an even Number.").format(i)
        elif i%2!=0 :
            print ("Number is {}. This is an odd Number.").format(i)
        i+=1

oddeven()
