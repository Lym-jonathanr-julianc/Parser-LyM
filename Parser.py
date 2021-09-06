import tokenize
import random
import nltk
from nltk.tokenize import MWETokenizer
matrix= []
robot= {"name": "robot", "direction":"north","chips": 0, "balloons":0}
matrixobj= []
def Move(n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
                direction= matrix[i][j]["direction"]
    
    matrix[coordinate1] [coordinate2]= None
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
        

def Right(n):
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
    

def Left(n):
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
        Left(n)
    else:
        Right(n)

def Look(o):
    if o == "N":
        robot["direction"] = "north"
    elif o == "E":
        robot["direction"]= "east"
    elif o == "W":
        robot["direction"]= "west"
    elif o == "S":
        robot["direction"]= "southt"

def drop(n):
    chips= robot["chips"]
    robot["chips"]= chips - n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["chips"]+= n 

def free(n):
    balloons= robot["balloons"]
    robot["balloons"]= balloons - n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["balloons"]+= n 

def pick(n):
    chips= robot["chips"]
    robot["chips"]= chips + n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["chips"]-= n 

def pop(n):
    balloons= robot["balloons"]
    robot["balloons"]= balloons + n
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    matrixobj[coordinate1][coordinate2]["balloons"]-= n

def check(o,n):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != None and matrix[i][j]["name"]=="robot":
                coordinate1= i
                coordinate2= j
    if o == "B":
        return matrixobj[coordinate1][coordinate2]["balloons"]
    else:
        return matrixobj[coordinate1][coordinate2]["chips"]

def blockedp():
    try:
        Move(1)
        return(True)
    except:
        return False

def nop():
    return None

def block(function, *args, **kwargs):
    function(*args, **kwargs)
    return function
    
def repeat(n, function, *args, **kwargs):
    n*function(*args, **kwargs)

def conditional(expr:bool, function, *args, **kwargs):
    return None

def define(n, val):
    try:
        val=0
        n=int(val)
        return val
    except:
        return "Esto no es un numero entero, intente de nuevo."

#------------------------Tokenizacion-Parser-------------------------------

tokenizer.add_mwe(blockedp())
def archivo(nombre_archivo:str):
    txtfile = open(nombre_archivo, "r")
    for x in txtfile:
        if tokenizer._mwes == x:
            print ("Yes")
        else:
            print("No")



        
