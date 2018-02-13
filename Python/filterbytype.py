def filter(variable):
    if (type(variable)==int):
        if(variable>=100):
            print "That's a big number!"
        elif (variable<100):
            print "That's a small number."

    if (type(variable)==str):
        if (len(variable)>=50):
            print "Long sentence"
        elif (len(variable)<50):
            print "Short sentence"

    if (type(variable)==list):
        if (len(variable)>=10):
            print "Big list"
        elif (len(variable)<10):
            print "Short list"




print filter(13)
print filter("hello wolrd")
print filter([1,2,3,4,5])
