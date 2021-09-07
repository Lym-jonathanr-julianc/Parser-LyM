
import random

robot= {"name": "robot", "direction":"north","chips": 0, "balloons":0}
matrix= [[robot,0,0],
        [0,0,0],
        [0,0,0]]
matrixobj= [[{},{"balloons" : 0, "chips" : 0}]]
def move(n:int):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                coordinate1= i
                coordinate2= j
                direction= matrix[i][j]["direction"]
    
    matrix[coordinate1] [coordinate2]= 0
    if direction == "north":
        newCordinate= coordinate1 + n
        matrix[ newCordinate] [coordinate2]= robot
    elif direction == "south":
        newCordinate= coordinate1 - n
        matrix[ newCordinate] [coordinate2]= robot
    elif direction == "east":
        newCordinate= coordinate2 + n
        matrix[coordinate1] [newCordinate]= robot
    elif direction == "west":
        newCordinate= coordinate2 - n
        matrix[coordinate1] [newCordinate]= robot
        

def right(n:int):
    if robot["direction"] == "north":
        if n <= 90:
            robot["direction"] = "east"
        elif n > 90 and n <= 180:
            robot["direction"]= "south"
        elif n > 180 and n <= 270:
            robot["direction"]= "west"
        else:
            pass
    elif robot["direction"] == "south":
            if n <= 90:
                robot["direction"] = "west"
            elif n > 90 and n <= 180:
                robot["direction"]= "north"
            elif n > 180 and n <= 270:
                robot["direction"]= "east"
            else:
                pass
    elif robot["direction"] == "west":
            if n <= 90:
                robot["direction"] = "north"
            elif n > 90 and n <= 180:
                robot["direction"]= "east"
            elif n > 180 and n <= 270:
                robot["direction"]= "south"
            else:
                pass
    elif robot["direction"] == "east":
            if n <= 90:
                robot["direction"] = "south"
            elif n > 90 and n <= 180:
                robot["direction"]= "west"
            elif n > 180 and n <= 270:
                robot["direction"]= "north"
            else:
                pass
    

def left(n:int):
   if robot["direction"] == "north":
        if n <= 90:
            robot["direction"] = "west"
        elif n > 90 and n <= 180:
            robot["direction"]= "south"
        elif n > 180 and n <= 270:
            robot["direction"]= "east"
        else:
            pass
   elif robot["direction"] == "south":
            if n <= 90:
                robot["direction"] = "east"
            elif n > 90 and n <= 180:
                robot["direction"]= "north"
            elif n > 180 and n <= 270:
                robot["direction"]= "west"
            else:
                pass
   elif robot["direction"] == "west":
            if n <= 90:
                robot["direction"] = "south"
            elif n > 90 and n <= 180:
                robot["direction"]= "east"
            elif n > 180 and n <= 270:
                robot["direction"]= "north"
            else:
                pass
   elif robot["direction"] == "east":
            if n <= 90:
                robot["direction"] = "north"
            elif n > 90 and n <= 180:
                robot["direction"]= "west"
            elif n > 180 and n <= 270:
                robot["direction"]= "south"
            else:
                pass

def rotate(n):
    d= ("left","right")
    selected= random.choice(d)
    if selected == "left":
        left(n)
    else:
        right(n)

def look(o:str):
    if o == "N":
        robot["direction"] = "north"
    elif o == "E":
        robot["direction"]= "east"
    elif o == "W":
        robot["direction"]= "west"
    elif o == "S":
        robot["direction"]= "southt"

def drop(n:int):
    chips= robot["chips"]
    robot["chips"]= chips - n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["chips"]+= n 

def free(n:int):
    balloons= robot["balloons"]
    robot["balloons"]= balloons - n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["balloons"]+= n 

def pick(n:int):
    chips= robot["chips"]
    robot["chips"]= chips + n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["chips"]-= n 

def pop(n:int):
    balloons= robot["balloons"]
    robot["balloons"]= balloons + n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["balloons"]-= n

def check(o:str,n:int):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                coordinate1= i
                coordinate2= j
    if o == "b":
        return matrixobj[coordinate1][coordinate2]["balloons"]==n
    elif o == "c":
        return matrixobj[coordinate1][coordinate2]["chips"]==n

def blockedp():
    try:
        move(1)
        return(True)
    except:
        return False

def nop():
    return None


def define(n, val):
    try:
        val=0
        n=int(val)
        return val
    except:
        return "Esto no es un numero entero, intente de nuevo."

def commands(token:list):
        if len(token)==1 and token != ")":
                x=token[0]+"()"

        elif len(token)==2:
            x=token[0]+"("+token[1]+")"
        
        elif len(token)==3:
            x=token[0]+"("+"'"+ token[1]+"'"+","+token[2]+")"
        else:
            pass
        exec(x)
def repeat(n, rlist):
    while n>0:
        block(rlist)
        n=n-1
def ifFunction(iflist):
    isBlock=False
    isRepeat= False
    blist=[]
    rlist=[]
    nrepeat= 0
    a= 0
    
    if iflist[0][0] == "!":
        iflist[0].pop(0)
        iflist[0].pop(1)
        
        if blockedp == False:
            for i in iflist:
                if isBlock:
                    if ")" in i:
                        isblock= False
                    blist.append(i)
                    if isblock == False:
                        block(blist)
                        blist=[]
                    continue 
                if isRepeat:
                    if ")" in i:
                        isRepeat= False
                    rlist.append(i)
                    if isRepeat== False:
                        repeat(nrepeat,blist)
                        rlist=[]
                    continue     
                if len(i) == 1 and i[0]=="[":
                    continue
                else:
                    if "block" in i:
                        isBlock= True
                        i.pop(0)
                        i.pop(1)
                        blist.append(i)
                        continue
                    if "repeat" in i:
                        isRepeat= True
                        i.pop(0)
                        i.pop(1)
                        nrepeat= i[0]
                        rlist.append(i)
                        continue
                    if i[0] == "[":
                        i.pop(0)
                    commands(i)
        else:
            pass
    else:
        iflist[0].pop(0)
        if blockedp:
            for i in iflist:
                if isBlock:
                    if ")" in i:
                        isblock= False
                    blist.append(i)
                    if isblock == False:
                        block(blist)
                        blist=[]
                    continue 
                if isRepeat:
                    if ")" in i:
                        isRepeat= False
                    rlist.append(i)
                    if isRepeat== False:
                        repeat(blist)
                        rlist=[]
                    continue     
                if len(i) == 1 and i[0]=="[":
                    continue
                else:
                    if "block" in i:
                        isBlock= True
                        i.pop(0)
                        i.pop(1)
                        blist.append(i)
                        continue
                    if "repeat" in i:
                        isRepeat= True
                        i.pop(0)
                        i.pop(1)
                        nrepeat= i[0]
                        rlist.append(i)
                        continue
                    if i[0] == "[":
                        i.pop(0)
                    commands(i)
        else:
            pass
def block(blist):
    isIf= False
    isrepeat= False
    iflist=[]
    rlist=[]
    nrepeat= 0
    for i in blist:
        if isIf:
            if "]" in i[-1]:
              isIf= False
            if i[0] == "]":
                continue
            i[-1]=i[-1].replace("]","")
            iflist.append(i)
            if isIf== False:
                ifFunction(iflist)
            continue
        if isrepeat:
            if ")" in i[-1]:
              isIf= False
            if i[0] == ")":
                continue
            i[-1]=i[-1].replace(")","")
            rlist.append(i)
            if isrepeat== False:
                repeat(nrepeat, rlist)
            continue
            
        if i[0] == "if":
            isIf= True
            i.pop(0)
            iflist.append(i)
            continue

        if "repeat" in i:
            isrepeat= True
            i.pop(0)
            i.pop(1)
            nrepeat=i[0]
            rlist.append(i)
            continue


        if ")" in i[-1]:
            i[-1].replace(")","")
        commands(i)
           


            

#------------------------Tokenizacion-Parser-------------------------------

def archivo(nombre_archivo:str):
    isblock= False
    isIf= False
    isrepeat= False
    istoend= False
    blist=[]
    rlist=[]
    iflist=[]
    nrepeat= 0
    vardict= []
    varlist= []
    name= None
    txtfile = open(nombre_archivo, "r")
    for x in txtfile:
            if isblock:
                if ")" in x:
                    isblock= False
                x=x.lower()
                token=x.split()
                blist.append(token)
                if isblock == False:
                    block(blist)
                    blist=[]
                continue  
            if isrepeat:
                if ")" in x:
                    isrepeat= False
                x=x.lower()
                token=x.split()
                rlist.append(token)
                if isrepeat == False:
                    block(nrepeat ,rlist)
                    rlist=[]
                continue     
            if isIf:
                if "]" in x[-1]:
                    isIf= False
                if x[0] == "]":
                    continue
                x[-1]=x[-1].replace("]","")
                iflist.append(x)
                if isIf== False:
                    ifFunction(iflist)
                continue   

            x=x.lower()
            token=x.split()
            if "(block" in token:
                isblock = True
                if len(token) == 1:
                    continue
                else:
                  token.pop(0)
                  token.pop(1)
                  blist.append(token)
                  continue
            if "(repeat" in token:
                isrepeat = True
                if len(token) == 1:
                    continue
                else:
                  token.pop(0)
                  token.pop(1)
                  nrepeat= token[0]
                  token.pop(0)
                  rlist.append(token)
                  continue
            if "if" in token:
                isIf = True
                x.pop(0)
                iflist.append(x)
                continue
            
            if token[0]== "define":
                vardict[token[1]]= token[2]
                continue
             

       
        

#-----------------------------------------------------------------------------
def ejecutar():
    nombre_archivo=input("Ingrese el nombre del archivo: ")
    try:
        archivo(nombre_archivo)
        print("Yes")
    except:
        print("No")
    
ejecutar()




