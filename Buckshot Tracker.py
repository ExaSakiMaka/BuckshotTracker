import os

Balles = []
Current = "?"
Loop = 1
FirstTurn = 1
    

while Loop == 1:
    if FirstTurn == 1:
        os.system('cls')
        blue =int(input("Blank : "))
        red =int(input("Live : "))
        numballes = int(blue) + int(red)
        Balles =["?"]*numballes
        FirstTurn = 0
        os.system('cls')
    
    if red == 0:
        Balles =["B"]*numballes
    elif blue == 0:
        Balles =["L"]*numballes
        
    if list.count(Balles,"L") == red:
        for i in range(len(Balles)):
            if Balles[i] == "?":
                Balles[i] = "B"
            else:
                pass
            
    elif list.count(Balles,"B") == blue:
        for i in range(len(Balles)):
            if Balles[i] == "?":
                Balles[i] = "L"
            else:
                pass
    
    print("",blue,"Blank\n",red,"Live\n",numballes,"Balles\n\nCurrent :",Balles[0],"\n",Balles,"\n")
    
    todo =input("1 : Phone \n2 : Beer/Shot \n3 : End Round \n4 : Exit \n")
    
    if todo == "1":
        os.system('cls')
        Pos = input("Position : ")
        Type = input("Type : ")
        Balles [int(Pos)-1]= Type
        
    elif todo == "2":
        "Current :",Balles[0]
        numballes = numballes - 1
        
        if Balles[0] == "?":
            Balles[0] = input("Blank or Live ? (B/L) : ")
            
        if Balles[0] == "B":
            blue = blue - 1
        elif Balles[0] == "L":
            red = red - 1
        del Balles [0]
        
    elif todo == "3":
        FirstTurn = 1
    elif todo == "4":
        Loop = 0
    
    if Balles == []:
        os.system('cls')
        Restart = input("Round Over \nRestart ? (Y/N) : ")
        if Restart == "Y":
            FirstTurn = 1
        elif Restart == "N":
            Balles = ["end"]
            Loop = 0
        
    os.system('cls')