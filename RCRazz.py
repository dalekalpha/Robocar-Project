import RPi.GPIO as GPIO
import sys, tty, termios, time
GPIO.setmode(GPIO.BCM)

#Define Pinout
LeftMotorEnable = 2
LeftMotorA = 24
LeftMotorB = 22
RightMotorEnable = 4
RightMotorA = 17
RightMotorB = 15

#PWM Values
Frequency = 50
speed = 0

#Setup
GPIO.setup(LeftMotorEnable,GPIO.OUT)
GPIO.setup(LeftMotorA,GPIO.OUT)
GPIO.setup(LeftMotorB,GPIO.OUT)
GPIO.setup(RightMotorEnable,GPIO.OUT)
GPIO.setup(RightMotorA,GPIO.OUT)
GPIO.setup(RightMotorB,GPIO.OUT)

#PWM
Left = GPIO.PWM(LeftMotorEnable,Frequency)
Right = GPIO.PWM(RightMotorEnable,Frequency)

#Basic Movement
def LeftForward(dutycycle):
	GPIO.output(LeftMotorA,GPIO.HIGH)
	GPIO.output(LeftMotorB,GPIO.LOW)
	Left.start(dutycycle)
	
def LeftReverse(dutycycle):
	GPIO.output(LeftMotorA,GPIO.LOW)
	GPIO.output(LeftMotorB,GPIO.HIGH)
	Left.start(dutycycle)
	
def RightForward(dutycycle):
	GPIO.output(RightMotorA,GPIO.HIGH)
	GPIO.output(RightMotorB,GPIO.LOW)
	Right.start(dutycycle)

def RightReverse(dutycycle):
	GPIO.output(RightMotorA,GPIO.LOW)
	GPIO.output(RightMotorB,GPIO.HIGH)
	Right.start(dutycycle)
	
def Stop():
	Left.start(0)
	Right.start(0)
	return;

#Remote Control Module
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

redo = False
lastcommand = ""
Stop()

#Remote Control Command input
while True:
	input = getch()
	if(input == "w"):
		lastcommand = "w"
		LeftForward(speed)
		RightForward(speed)
		redo = False
	if(input == "s"):
		lastcommand = "s"
		LeftReverse(speed)
		RightReverse(speed)
		redo = False
	if(input == "q"):
		lastcommand = "q"
		LeftReverse(speed)
		RightForward(speed)
		redo = False
	if(input == "e"):
		lastcommand = "e"
		LeftForward(speed)
		RightReverse(speed)
		redo = False
	if(input == "a"):
		lastcommand = "a"
		Left.start(speed/2)
		Right.start(speed)
		redo = False
	if(input == "d"):
		lastcommand = "d"
		Left.start(speed)
		Right.start(speed/2)
		redo = False
	
	if( input == "1" ):
		speed = 10
		redo = True
	if( input == "2" ):
		speed = 20
		redo = True
	if( input == "3" ):
		speed = 30
		redo = True
	if( input == "4" ):
		speed = 40
		redo = True
	if( input == "5" ):
		speed = 50
		redo = True
	if( input == "6" ):
		speed = 60
		redo = True
	if( input == "7" ):
		speed = 70
		redo = True
	if( input == "8" ):
		speed = 80
		redo = True
	if( input == "9" ):
		speed = 90
		redo = True
	if( input == "0" ):
		speed = 100
		redo = True
	
	if(input == "x"):
		break
	if(input == "z"):
		lastcommand = "z"
		Stop()
	if(redo == True):
		input = lastcommand
	if(redo == False):
		input = ""
		
input = ""
GPIO.cleanup():