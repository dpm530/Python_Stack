import random
def testscores():
    i=0
    while i<10:
        rand_int=random.randint(60,101)
        if rand_int>60 and rand_int<70 :
            print ("Score:{}; Your grade is D").format(rand_int)
        elif rand_int>=70 and rand_int<80 :
            print ("Score:{}; Your grade is C").format(rand_int)
        elif rand_int>=80 and rand_int<90 :
            print ("Score:{}; Your grade is B").format(rand_int)
        elif rand_int>=90 and rand_int<=100 :
            print ("Score:{}; Your grade is A").format(rand_int)
        i+=1

testscores()
