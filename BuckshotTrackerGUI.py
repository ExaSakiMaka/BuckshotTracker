import tkinter as tk
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

def DefineGlobalVar(Balles,Blanks,Lives,numballes):
        global GlobalBlanks
        GlobalBlanks = Blanks
        
        global GlobalLives
        GlobalLives = Lives
        
        global GlobalBalles
        GlobalBalles = Balles
        
        global Globalnumballes
        Globalnumballes = numballes

def startround():
    Blanks =app.BlankVar.get() #Number of Blanks
    Lives =app.LiveVar.get() #Number of Lives
    numballes = int(Blanks) + int(Lives) #Calculating Number of Bullets
    Balles =["?"]*numballes #Initializing the list
        
    DefineGlobalVar(Balles,Blanks,Lives,numballes)   
    app.withdraw()

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Round Window")
        self.geometry("265x550")
        self.grid_columnconfigure(0, weight=1)
        #self.grid_rowconfigure(0, weight=1)
        self.resizable(False, False)
        
        self.topframe =customtkinter.CTkFrame(self) #initializing the top frame
        self.topframe.grid(row=0, column=0, padx=10, pady=10)
        self.Blanktxt = customtkinter.CTkLabel(self.topframe, text="Blanks : " + GlobalBlanks, font=("Roboto", 20),text_color="blue")
        self.LiveTxt = customtkinter.CTkLabel(self.topframe, text="Lives : " + GlobalLives, font=("Roboto", 20),text_color="red")
        self.Bulletlist = customtkinter.CTkLabel(self.topframe, text="Bullets : " + str(GlobalBalles), font=("Roboto", 20))
        
        self.phoneframe =customtkinter.CTkFrame(self) #initializing the phone frame
        self.phoneframe.grid(row=1, column=0, padx=10, pady=10)
        self.PhoneLabel = customtkinter.CTkLabel(self.phoneframe, text="Phone", font=("Roboto", 20))
        self.shotselectorvar =customtkinter.StringVar(value="")
        self.shotselector =customtkinter.CTkSegmentedButton(self.phoneframe, values=[], font=("Roboto", 12), variable=self.shotselectorvar)
        for i in range(len(GlobalBalles)):
            self.shotselector.insert(i, str(i+1))
        self.optionmenu_var = customtkinter.StringVar(value="Choose Type")
        self.optionmenu = customtkinter.CTkOptionMenu(self.phoneframe,values=["Live", "Blank", "????"],variable=self.optionmenu_var)
        self.ApplyButton = customtkinter.CTkButton(self.phoneframe, text="Apply", command=self.SelectShot, font=("Roboto", 12))
        
        self.ejectframe =customtkinter.CTkFrame(self) #initializing the eject frame
        self.ejectframe.grid(row=2, column=0, padx=10, pady=10)
        self.ejectlabel = customtkinter.CTkLabel(self.ejectframe, text="Ejecting", font=("Roboto", 20))
        self.BlankorLivevar =customtkinter.StringVar(value="")
        self.BlankorLive =customtkinter.CTkSegmentedButton(self.ejectframe, values=["Blank", "Live"], variable=self.BlankorLivevar )
        self.ejectbutton =customtkinter.CTkButton(self.ejectframe, text="eject",command=self.EjectBullet,font=("Roboto", 12))
        
        self.exitbutton = customtkinter.CTkButton(master=self, text="Exit", command=self.exitround, font=("Roboto", 12)) #exit button
        
        self.PhoneLabel.grid(row=0, column=0, padx=10, sticky="ew", columnspan=2)
        self.Blanktxt.grid(row=0, column=0, padx=10, sticky="ew")
        self.LiveTxt.grid(row=0, column=1, padx=10, sticky="ew")
        self.Bulletlist.grid(row=1, column=0, padx=10,columnspan=2, sticky="ew",)
        self.shotselector.grid(row=2, column=0, padx=10, columnspan=2, sticky="ew")
        self.optionmenu.grid(row=3, column=0, padx=10,pady=10, columnspan=2, sticky="ew")
        self.ApplyButton.grid(row=4, column=0, padx=10,pady=10, columnspan=2, sticky="ew")
        
        self.ejectframe.grid(row=4, column=0, padx=10, pady=10)
        self.ejectlabel.grid(row=5, padx=10,pady=10,columnspan=2,sticky="ew")
        self.BlankorLive.grid(row=6, column=0, padx=10,pady=10, columnspan=2, sticky="ew")
        self.ejectbutton.grid(row=7,column=0,padx=10,pady=10, columnspan=2, sticky="ew")
        self.exitbutton.grid(row=8, column=0, padx=10,pady=(40,0), columnspan=2, sticky="ew")
        
    def autofiller(self,Balles,Blanks,Lives,numballes):
        
        print("balles start :", Balles)
        print("blanks count :",list.count(Balles,"B"))
        print("blanks var :", Blanks)
        print("lives count :",list.count(Balles,"L"))
        print("lives var :", Lives)
        print("numballes var :", numballes)
        
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
        self.Bulletlist.configure(text="Bullets : " + str(Balles))
        self.Blanktxt.configure(text="Blank : " + str(Blanks))
        self.LiveTxt.configure(text="Live : " + str(Lives))
        
        if list.count(Balles,"?") == 0:
                self.BlankorLive.destroy()
                self.ApplyButton.destroy()
                self.optionmenu.destroy()
                        
        DefineGlobalVar(Balles,Blanks,Lives,numballes)
    
    def SelectShot(self):
        pos = self.shotselectorvar.get()
        type = self.optionmenu_var.get()
        
        GlobalBalles[int(pos)-1] = type[0]
        self.autofiller(GlobalBalles,int(GlobalBlanks),int(GlobalLives),int(Globalnumballes))
        
    def EjectBullet(self,):
        listeTemp=[]
        Balles = GlobalBalles
        Blanks = int(GlobalBlanks)
        Lives = int(GlobalLives)
        numballes = int(Globalnumballes)
        
        self.shotselector.delete(str(numballes-(numballes-1))) #resizing the phone selector
        
        if list.count(Balles,"?") == 0: #if allthe bullets are knownin the list
                Current = Balles[0] #just read the first entry
        else: #if not
                Current = self.BlankorLivevar.get() #read the selected bullet
                
        print(Current[0])
        Balles[0] = str(Current[0])
        numballes = numballes - 1
            
        if Balles[0] == "B": #then updates the list
            Blanks = Blanks - 1
            del Balles [0]
            
        elif Balles[0] == "L":
            Lives = Lives - 1
            del Balles [0]
            
        if Balles == []:
            self.exitround()
        
        
        for i in range(numballes):
            listeTemp.append(str(i+1))
        
        self.shotselector.configure(values=listeTemp)
            
        DefineGlobalVar(Balles,Blanks,Lives,numballes)
        self.autofiller(Balles,int(Blanks),int(Lives),int(numballes))
    
    def exitround(self):
        app.deiconify()
        self.destroy()
    
class App(customtkinter.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Buckshot Tracker")
        self.geometry("340x150")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.resizable(False, False)

        self.frameacceuil = customtkinter.CTkFrame(self)
        
        self.BlankVar = tk.StringVar()
        self.BlankWidget = customtkinter.CTkEntry(self.frameacceuil, placeholder_text="Blank", textvariable=self.BlankVar, font=("Roboto", 12))
        self.BlankLabel = customtkinter.CTkLabel(self.frameacceuil, text="Blank", font=("Roboto", 20),text_color="blue")
        
        self.LiveVar = tk.StringVar()
        self.LiveWidget = customtkinter.CTkEntry(self.frameacceuil, placeholder_text="Live", textvariable=self.LiveVar, font=("Roboto", 12))
        self.LiveLabel = customtkinter.CTkLabel(self.frameacceuil, text="Live", font=("Roboto", 20),text_color="red")

        self.start = customtkinter.CTkButton(master=self, text="Start", command=self.open_toplevel, font=("Roboto", 12))
        self.toplevel_window = None
        
        self.frameacceuil.grid(row=1, column=0, padx=10, pady=10, sticky="nsew",columnspan=2)
        
        self.BlankWidget.grid(row=1, column=0, padx=10,pady=(10,0),sticky="ew")
        self.BlankLabel.grid(row=2, column=0, padx=10,sticky="ew")
        
        self.LiveWidget.grid(row=1, column=1, padx=10,pady=(10,0),sticky="ew")
        self.LiveLabel.grid(row=2, column=1, padx=10,sticky="ew")
        
        self.start.grid(row=3, column=0, padx=0,pady=(30,0), columnspan=2, sticky="ew")
        
    def open_toplevel(self):
        startround()
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it 
        
app =App()
app.mainloop()
