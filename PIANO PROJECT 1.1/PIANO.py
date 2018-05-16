import pygame
from Tkinter import *
import RPi.GPIO as GPIO
from time import sleep

pygame.init()

#set the GPIO pin numbers
#the LEDs (from Lto R)
leds = [6, 13, 19, 21, 16, 20, 12, 24, 5, 22, 26, 4, 23]

#use the Broadcom pin mode
GPIO.setmode(GPIO.BCM)

#setup the input and output pins
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#when a button is pressed, the corresponding command plays
def value_Cs():
    sound = pygame.mixer.Sound("c1s.wav")
    #turn the appropriate LED on
    GPIO.output(leds[8], True)
    #play its corresponding sound
    sound.play()
    #wait and turn the LED off again
    sleep(.5)
    GPIO.output(leds[8], False)
    
def value_Ds():
    sound = pygame.mixer.Sound("d1s.wav")
    sound.play()
    GPIO.output(leds[9], True)
    sleep(.5)
    GPIO.output(leds[9], False)
    
def value_Fs():
    sound = pygame.mixer.Sound("f1s.wav")
    sound.play()
    GPIO.output(leds[10], True)
    sleep(.5)
    GPIO.output(leds[10], False)
    
def value_Gs():
    sound = pygame.mixer.Sound("g1s.wav")
    sound.play()
    GPIO.output(leds[11], True)
    sleep(.5)
    GPIO.output(leds[11], False)
    
def value_Bb():
    sound = pygame.mixer.Sound("a1s.wav")
    sound.play()
    GPIO.output(leds[12], True)
    sleep(.5)
    GPIO.output(leds[12], False)

def value_C():
    sound = pygame.mixer.Sound("c1.wav")
    sound.play()
    GPIO.output(leds[0], True)
    sleep(.5)
    GPIO.output(leds[0], False)
    
def value_D():
    sound = pygame.mixer.Sound("d1.wav")
    sound.play()
    GPIO.output(leds[1], True)
    sleep(.5)
    GPIO.output(leds[1], False)
    
def value_E():
    sound = pygame.mixer.Sound("e1.wav")
    sound.play()
    GPIO.output(leds[2], True)
    sleep(.5)
    GPIO.output(leds[2], False)
    
def value_F():
    sound = pygame.mixer.Sound("f1.wav")
    sound.play()
    GPIO.output(leds[3], True)
    sleep(.5)
    GPIO.output(leds[3], False)
    
def value_G():
    sound = pygame.mixer.Sound("g1.wav")
    sound.play()
    GPIO.output(leds[4], True)
    sleep(.5)
    GPIO.output(leds[4], False)
    
def value_A():
    sound = pygame.mixer.Sound("a1.wav")
    sound.play()
    GPIO.output(leds[5], True)
    sleep(.5)
    GPIO.output(leds[5], False)
    
def value_B():
    sound = pygame.mixer.Sound("b1.wav")
    sound.play()
    GPIO.output(leds[6], True)
    sleep(.5)
    GPIO.output(leds[6], False)
    
def value_C2():
    sound = pygame.mixer.Sound("c2.wav")
    sound.play()
    GPIO.output(leds[7], True)
    sleep(.5)
    GPIO.output(leds[7], False)

#plays part of row row row your boat when button pressed   
def check_switch():
    value_C()
    sleep(.2)
    value_C()
    sleep(.2)
    value_C()
    sleep(.1)
    value_D()
    sleep(.05)
    value_E()
    sleep(.01)
    value_E()
    sleep(.2)
        
    value_D()
    sleep(.1)
    value_E()
    sleep(.3)
    value_F()
    sleep(.1)
    value_G()
    sleep(1)
    
root = Tk()
frame = Frame(root)
frame.pack()

root.title("Piano")

topframe = Frame(root)
topframe.pack(side = TOP)

#makes the button on the top to play a song
playsong = Button(frame, padx = 10, height = 1, pady=10, bg ="black", fg = "white", command= check_switch)
playsong.pack(side =LEFT)

#Makes Cs key
Cs = Button(topframe, padx=8, height=6, pady=8, text="C# ", bg="black", fg="white", command=value_Cs)
Cs.pack(side =LEFT)

#makes a random unusable button in order to correctly space keys
button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side = LEFT)

#makes Ds key
Ds = Button(topframe, padx=8, height=6, pady=8, text="D# ", bg="black", fg="white", command=value_Ds)
Ds.pack(side = LEFT)

#makes a random unusable button in order to correctly space keys
button22 = Button(topframe, state=DISABLED, height=7, width=5, padx=0, pady=0, relief=RIDGE)
button22.pack(side = LEFT)

#makes Fs key
Fs = Button(topframe, padx=8, height=6, pady=8, text="F# ", bg="black", fg="white", command=value_Fs)
Fs.pack(side = LEFT)

#makes a random unusable button in order to correctly space keys
button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side = LEFT)

#makes Gs key
Gs = Button(topframe, padx=8, height=6, pady=8, text="G# ", bg="black", fg="white", command=value_Gs)
Gs.pack(side = LEFT)

#makes a random unusable button in order to correctly space keys
button22 = Button(topframe, state=DISABLED, height=7, width=1, padx=0, pady=0, relief=RIDGE)
button22.pack(side = LEFT)

#makes the Bb key
Bb = Button(topframe, padx=8, height=6, pady=8, text="Bb ", bg="black", fg="white", command=value_Bb)
Bb.pack(side = LEFT)

frame1 = Frame(root)
frame1.pack(side = TOP)

#makes the first C key
C = Button(frame1, padx=16, height=8, bd=8, pady=16, text="C", fg="black", command=value_C)
C.pack(side = LEFT)

#makes the D key
D = Button(frame1, padx=16, height=8, bd=8, pady=16, text="D", fg="black", command=value_D)
D.pack(side = LEFT)

#makes the E key
E = Button(frame1, padx=16, height=8, bd=8, pady=16, text="E", fg="black", command=value_E)
E.pack(side = LEFT)

#makes the F key
F = Button(frame1, padx=16, height=8, bd=8, pady=16, text="F", fg="black", command=value_F)
F.pack(side = LEFT)

#makes the G key
G = Button(frame1, padx=16, height=8, bd=8, pady=16, text="G", fg="black", command=value_G)
G.pack(side = LEFT)

#makes the A key
A = Button(frame1, padx=16, height=8, bd=8, pady=16, text="A", fg="black", command=value_A)
A.pack(side = LEFT)

#makes the B key
B = Button(frame1, padx=16, height=8, bd=8, pady=16, text="B", fg="black", command=value_B)
B.pack(side = LEFT)

#makes the second C key
C1 = Button(frame1, padx=16, height=8, bd=8, pady=16, text="C", fg="black", command=value_C2)
C1.pack(side = LEFT)

root.mainloop()
