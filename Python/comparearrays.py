def compare(list1,list2):
    list1.sort()
    list2.sort()
    if list1 == list2:
        print "true"
        return True
    else:
        print "false"
        return False


compare([1,2,5,6,2],[1,2,5,6,2])
compare([1,2,5,6,5],[1,2,5,6,5,3])
compare([1,2,5,6,5,16],[1,2,5,6,5])
compare(['celery','carrots','bread','milk'],['celery','carrots','bread','cream'])
