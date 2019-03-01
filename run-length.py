runList = 'cccccbbrpppzzzzzza'
l = "abcdefghijklmnopqrstuvwxyz"
finalList = []
for x in l:
    # print(x)
    if runList.count(x) > 0:
        item = x + str(runList.count(x))
        finalList.append(item)    
        print(*finalList, sep ='') 
