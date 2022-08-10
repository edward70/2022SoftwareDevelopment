import sys
readline = sys.stdin.readline

lines = [readline()[0:-1] for i in range(int(readline()))]

def partial_algorithm(string):
    #breakpoint()
    oldstring = string
    string = string[1:]
    first_letter = oldstring[0]
    poslst = []
    for i,char in enumerate(string):
        if char == first_letter:
            poslst.append(i)
    if len(poslst) == 0:
        return (0, oldstring)
    
    x = 1
    while x < len(string):
        x_letter = oldstring[x]
        newpos = []
        for pos in poslst:
            if pos+1 < len(string) and string[pos+1] == x_letter and pos+1 > x:
                newpos.append(pos)
        if len(newpos) == 0:
            poslst = [(a+1)//2 for a in poslst]
            x //= 2
            return (x, oldstring[x:])
        else:
            poslst = [a*2+1 for a in newpos]
            x *= 2
    return (x, oldstring[x:])

def full_algorithm(string):
    x, string = partial_algorithm(string)
    while x > 0:
        x, string = partial_algorithm(string)
    print(string)

for line in lines:
    full_algorithm(line)
