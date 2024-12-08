import os #importing os module to clear the screen

Loop = 1
FirstTurn = 1 #initializing Basic Variables

    

while Loop == 1:
    if FirstTurn == 1:
        os.system('cls')
        Blanks =int(input("Blank : ")) #Number of Blanks
        Lives =int(input("Live : ")) #Number of Lives
        numballes = int(Blanks) + int(Lives) #Calculating Number of Bullets
        Balles =["?"]*numballes #Initializing the list
        FirstTurn = 0
        os.system('cls')
    
    if Lives == 0: #If no lives left fill the list with blanks
        Balles =["B"]*numballes
    elif Blanks == 0: #if no blanks left fill the list with lives
        Balles =["L"]*numballes
        
    if list.count(Balles,"L") == Lives: #If all lives are in the list fill the missing bullets with blanks
        for i in range(len(Balles)):
            if Balles[i] == "?":
                Balles[i] = "B"
            
    elif list.count(Balles,"B") == Blanks: #If all blanks are in the list fill the missing bullets with lives
        for i in range(len(Balles)):
            if Balles[i] == "?":
                Balles[i] = "L"

    #Calculating percentages
    BlankPercent = round(Blanks*100/numballes)
    LivePercent = round(Lives*100/numballes)
    
    #Printing the interface
    print("",Blanks,"Blank\n",Lives,"Live\n",numballes,"Balles\n\nCurrent :",Balles[0],"\n",Balles,"\n")
    print("Next shot :\nBlank :",str(BlankPercent)+"%\nLive : "+str(LivePercent)+"%\n")
    
    todo =input("1 : Phone \n2 : Beer/Shot \n3 : End Round \n4 : Exit \n")
    
    if todo == "1": #asks for position and type of the bullet to place it in the list
        os.system('cls')
        Pos = input("Position : ")
        Type = input("Type : ")
        Balles [int(Pos)-1]= Type
        
    elif todo == "2":
        os.system('cls')
        "Current :",Balles[0] #removes the first bullet
        numballes = numballes - 1
        
        if Balles[0] == "?": #if the shot is unknown asks for the type
            Balles[0] = input("Blank or Live ? (B/L) : ")
            
        if Balles[0] == "B": #then updates the list
            Blanks = Blanks - 1
        elif Balles[0] == "L":
            Lives = Lives - 1
        del Balles [0]
        
    elif todo == "3":
        FirstTurn = 1 #restarts the game
    elif todo == "4":
        Loop = 0 #ends the game
    
    if Balles == []: #simple auto restart
        os.system('cls')
        Restart = input("Round Over \nRestart ? (Y/N) : ")
        if Restart == "Y":
            FirstTurn = 1
        elif Restart == "N":
            Balles = ["end"]
            Loop = 0
        
    os.system('cls')
