###################################################
#Name: Tracy Samanie
#Date: February 9, 2018
#Description: The Reckoner (CSC 131)
###################################################

from Tkinter import *

result = 0
#main GUI
class MainGUI(Frame):
    #the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", True)
        self.setupGUI()

   #sets up the GUI
    def setupGUI(self):
        #sets up the display
##        self.display = Label(self, text="", anchor=E, bg="white", \
##                            height=0, width=14, font=("TexGyreAdventor", 45))
##        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        #there are 6 rows (0 through 6)
        for row in range(5):
            Grid.rowconfigure(self, row, weight=1)
        #there are 4 columns (0 through 3)
        for col in range(13):
            Grid.columnconfigure(self, col, weight=1)

            
        #white keys
        # C
        #get the image
        img = PhotoImage(file="images/white2.gif")
        #create the button
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("("))
        #set the buttons image
        button.image = img
        #put the button in the correct place
        button.grid(row=3, rowspan=3,  column=0, columnspan=2, sticky=N+S+E+W)

        # D
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process(")"))
        button.image = img
        button.grid(row=3, rowspan=3, column=2, columnspan=2, sticky=N+S+E+W)

        # E
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("AC"))
        button.image = img
        button.grid(row=3, rowspan=3, column=4, columnspan=2, sticky=N+S+E+W)

        # F
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("back"))
        button.image = img
        button.grid(row=3, rowspan=3, column=6, columnspan=2, sticky=N+S+E+W)


        # G
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("7"))
        button.image = img
        button.grid(row=3, rowspan=3, column=8, columnspan=2, sticky=N+S+E+W)

        # A
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("8"))
        button.image = img
        button.grid(row=3, rowspan=3, column=10, columnspan=2, sticky=N+S+E+W)

        # C
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=3, rowspan=3, column=12, columnspan=2, sticky=N+S+E+W)

        # black keys
        # C#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=1, rowspan=2, column=1, columnspan=2, sticky=N+S+E+W)

        # D#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=1, rowspan=2, column=3, columnspan=2, sticky=N+S+E+W)

        # F#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=1, rowspan=2, column=7, columnspan=2, sticky=N+S+E+W)
        
        # G#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=1, rowspan=2, column=9, columnspan=2, sticky=N+S+E+W)

        # Bb
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=1, rowspan=2, column=11, columnspan=2, sticky=N+S+E+W)

        
        #pack the GUI
        self.pack(fill=BOTH, expand=1)
        
    
    #processes button presses
    def process(self, button):
        
        #AC clears the display
        if (button == "AC"):
            #clear the display
            self.display["text"] = ""
        
        #back: clears the last number of the character
        elif(button == "back"):
            self.display["text"] = str(self.display["text"])[:-1]
        
        # = starts an evaluation of whatever is on the display
        elif (button == "="):
            #get the expression in the display
            expr = self.display["text"]
            #the evaluation may return an error!
            try:
                #evaluate the expression
                global result
                result = eval(expr)
                #store the result to the display
                self.display["text"] = str(result)
                if (len(str(result)) >= 14):
                    self.display["text"] = str(result)[0:11] + "..."
            #handle if an error occurs during evaluation

            except:
                #note the error in the display
                self.display["text"] = "ERROR"
                
                
                
        #clear after result displayed       
        elif self.display["text"] == "ERROR":
            if button:
                self.display["text"] = ""
                self.display["text"] = button
        elif self.display["text"] == str(result):
            if button:
                self.display["text"] = ""
                self.display["text"] = button 
        elif self.display["text"] == (str(result)[0:11] + "..."):
            if button:
                self.display["text"] = ""
                self.display["text"] = button 
           
                            
        #otherwise, just tack on the appropriate operand/operator until 14 characters reached
        else:
            while (len(self.display["text"]) <= 13):
                self.display["text"] += button
                break

###############################################
# MAIN PART OF THE PROGRAM
###############################################

#create the window
window = Tk()
#set the title
window.title("The Reckoner")
#generate the GUI
p = MainGUI(window)
#display the GUI
window.mainloop()
