###################################################
#Name: 
#Date: 
#Description: 
###################################################
import RPi.GPIO as GPIO
from time import sleep
import pygame
from random import randint
from Tkinter import *

###set to True to enable debugging output
##DEBUG = True

#initilize the pygame library
pygame.init()

#set the GPIO pin numbers
#the LEDs (from Lto R)
leds = [6, 13, 19, 21, 16, 20, 12, 5, 22, 26, 4, 23]

#the sounds that map to each key / LED (from L to R) W then B 
sounds = [ pygame.mixer.Sound("one.wav"), \
           pygame.mixer.Sound("two.wav"), \
           pygame.mixer.Sound("three.wav"), \
           pygame.mixer.Sound("four.wav"), \
           pygame.mixer.Sound("one.wav"), \
           pygame.mixer.Sound("two.wav"), \
           pygame.mixer.Sound("three.wav"), \
           pygame.mixer.Sound("four.wav"), \
           pygame.mixer.Sound("one.wav"), \
           pygame.mixer.Sound("two.wav"), \
           pygame.mixer.Sound("three.wav"), \
           pygame.mixer.Sound("four.wav")]


#use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

#setup the input and output pins
#GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

###this function turns the LEDs on
##def all_on():
##    for i in leds:
##        GPIO.output(leds, True)
##
###this function turns the LEDs off
##def all_off():
##    for i in leds:
##        GPIO.output(leds, False)
##
###this function flashes the LEDs a few times when the player loses the game
##def lose():
##    for i in range(0, 12):
##        all_on()
##        sleep(0.5)
##        all_off()
##        sleep(0.5)


#result = 0
#main GUI
class MainGUI(Frame):
    #the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", True)
        self.setupGUI()

   #sets up the GUI
    def setupGUI(self):

        #there are 6 rows (0 through 6)
        for row in range(5):
            Grid.rowconfigure(self, row, weight=1)
        #there are 4 columns (0 through 3)
        for col in range(14):
            Grid.columnconfigure(self, col, weight=1)

            
        #white keys
        # C
        #get the image
        img = PhotoImage(file="images/white2.gif")
        #create the button
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("C"))
        #set the buttons image
        button.image = img
        #put the button in the correct place
        button.grid(row=3, rowspan=3,  column=0, columnspan=2, sticky=N+S+E+W)

        # D
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("D"))
        button.image = img
        button.grid(row=3, rowspan=3, column=2, columnspan=2, sticky=N+S+E+W)

        # E
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("E"))
        button.image = img
        button.grid(row=3, rowspan=3, column=4, columnspan=2, sticky=N+S+E+W)

        # F
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("F"))
        button.image = img
        button.grid(row=3, rowspan=3, column=6, columnspan=2, sticky=N+S+E+W)


        # G
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("G"))
        button.image = img
        button.grid(row=3, rowspan=3, column=8, columnspan=2, sticky=N+S+E+W)

        # A
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("A"))
        button.image = img
        button.grid(row=3, rowspan=3, column=10, columnspan=2, sticky=N+S+E+W)

        # B
        img = PhotoImage(file="images/white2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("B"))
        button.image = img
        button.grid(row=3, rowspan=3, column=12, columnspan=2, sticky=N+S+E+W)

        # black keys
        # C#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("C#"))
        button.image = img
        button.grid(row=1, rowspan=2, column=1, columnspan=2, sticky=N+S+E+W)

        # D#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("D#"))
        button.image = img
        button.grid(row=1, rowspan=2, column=3, columnspan=2, sticky=N+S+E+W)

        # F#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("F#"))
        button.image = img
        button.grid(row=1, rowspan=2, column=7, columnspan=2, sticky=N+S+E+W)
        
        # G#
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("G#"))
        button.image = img
        button.grid(row=1, rowspan=2, column=9, columnspan=2, sticky=N+S+E+W)

        # Bb
        img = PhotoImage(file="images/black1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0,\
                        activebackground="white", command=lambda: self.process("Bb"))
        button.image = img
        button.grid(row=1, rowspan=2, column=11, columnspan=2, sticky=N+S+E+W)

        
        #pack the GUI
        self.pack(fill=BOTH, expand=1)
        
    #processes button presses
    def process(self, button):
        
        #Plays C if button pressed
        if (button == "C"):
            sound = pygame.mixer.Sound("one.wav")
            #play sound
            sound.play()
            #turn the appropriate LED on
            GPIO.output(leds[0], True)
            #wait and turn the LED off again
            sleep(1)
            GPIO.output(leds[0], False)
            sleep(0.5)

        #Plays D if button pressed
        elif (button == "D"):
            sound = pygame.mixer.Sound("one.wav")
            #turn the appropriate LED on
            GPIO.output(leds[1], True)
            #play its corresponding sound
            sound.play()
            #wait and turn the LED off again
            sleep(1)
            GPIO.output(leds[1], False)
            sleep(0.5)
            

##        
##        #back: clears the last number of the character
##        elif(button == "back"):
##            self.display["text"] = str(self.display["text"])[:-1]
##        
##        # = starts an evaluation of whatever is on the display
##        elif (button == "="):
##            #get the expression in the display
##            expr = self.display["text"]
##            #the evaluation may return an error!
##            try:
##                #evaluate the expression
##                global result
##                result = eval(expr)
##                #store the result to the display
##                self.display["text"] = str(result)
##                if (len(str(result)) >= 14):
##                    self.display["text"] = str(result)[0:11] + "..."
##            #handle if an error occurs during evaluation
##
##            except:
##                #note the error in the display
##                self.display["text"] = "ERROR"
##                
##                
##                
##        #clear after result displayed       
##        elif self.display["text"] == "ERROR":
##            if button:
##                self.display["text"] = ""
##                self.display["text"] = button
##        elif self.display["text"] == str(result):
##            if button:
##                self.display["text"] = ""
##                self.display["text"] = button 
##        elif self.display["text"] == (str(result)[0:11] + "..."):
##            if button:
##                self.display["text"] = ""
##                self.display["text"] = button 
##           
##                            
##        #otherwise, just tack on the appropriate operand/operator until 14 characters reached
##        else:
##            while (len(self.display["text"]) <= 13):
##                self.display["text"] += button
##                break
##
###the main part of the program initialize the sequence, each
###item in the sequence represents an LED (or key), indexed at 0 through 3
##seq = []
###randomly add the first two items to the sequence
##seq.append(randint(0,3))
##seq.append(randint(0,3))
##print "Welcome!"
##print "Try to play the sequence back by pressing the keys."
##print "Press Ctrl+C to exit..."

###we'll discuss this later, but this allows us to detect when
###Ctrl+C is pressed so that we can reset the GPIO pins
##try:
##    #keep going until the user presses Ctrl+C
##    while(True):
##        #randomly add one more item to the sequence
##        seq.append(randint(0,11))
##        if (DEBUG):
##            #display the sequence to the console
##            if (len(seq) > 11):
##                print
##            print "seq={}".format(seq)
##        #display the sequence using the LEDs
##        for s in seq:
##            #turn the appropriate LED on
##            GPIO.output(leds[s], True)
##            #play its corresponding sound
##            sounds[s].play()
##            #wait and turn the LED off again
##            sleep(1)
##            GPIO.output(leds[s], False)
##            sleep(0.5)

###
### NEED TO GET BUTTONS ON GUI TO WORK AS THE "SWITCHES"
#####
##            
##        #wait for player input (via the keys)
##        #initialize the count of keys pressed to 0
##        button_count = 0
##        #keep accepting player input until the number of items in the sequence is reached
##        while (button_count < len(seq)):
##            #initially note that no switch is pressed this will help with debouncing
##            pressed = False
##            #so long as no key is currently pressed
##            while (not pressed):
##                #.. we can check the status of each key
##                for i in range(len(buttons)):
##                    #if one key is pressed
##                    while ((buttons[i]) == True):
##                        #note its index
##                        val = i
##                        #note that a key has now been pressed
##                        #so that we don't detect any more keys pressed
##                        pressed = True
##                        
##            if (DEBUG):
##                #display the index of the key pressed
##                print val,
##
##            #light the matching LED
##            GPIO.output(leds[val], True)
##            #play its corresponding sound
##            sounds[val].play()
##            #wait and turn the LED off again
##            sleep(1)
##            GPIO.output(leds[val], False)
##            sleep(0.25)
##
##            #check to see if this LED is correct in the sequence
##            if (val != seq[button_count]):
##                #player is incorrect; invoke the lose function
##                lose()
##                #reset the GPIO pins
##                GPIO.cleanup()
##                #exit the game
##                exit(0)
##
##            #if the player has this item in the sequence correct, increment the count
##            button_count += 1
##            
###detect Ctrl+C
##except KeyboardInterrupt:
##    #reset the GPIO pins
##    GPIO.cleanup()


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
