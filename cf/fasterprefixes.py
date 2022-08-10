import sys
readline = sys.stdin.readline
 
lines = [readline()[0:-1] for i in range(int(readline()))]
for line in lines:
    length = len(line)
    x = length
    while x > 0:
        search_space = line[1:]
        substr = line[:x]
        if search_space.find(substr) != -1:
            line = line[x:]
            length = length - x
            x = length
        else:
            x-=1
            
    print(line)
