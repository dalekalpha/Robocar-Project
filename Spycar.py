import RPi.GPIO as IO
import pygame

pygame.init()
pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])

LeftMotorEnable = 
LeftMotorFront = 
LeftMotorRear = 
RightMotorEnable = 
RightMotorFront = 
RightMotorRear = 
ServoPan =
ServoPitch =


Frequency = 50
Speed = 0

IO.setup(LeftMotorEnable, IO.OUT)
IO.setup(LeftMotorFront, IO.OUT)
IO.setup(LeftMotorRear, IO.OUT)
IO.setup(RightMotorEnable, IO.OUT)
IO.setup(RightMotorFront, IO.OUT)
IO.setup(RightMotorRear, IO.OUT)

Left = IO.PWM(LeftMotorEnable, Frequency)
Right = IO.PWM(RightMotorEnable, Frequency)

Statey = 2
Statex = 2


while (True):
	Event = pygame.event.poll()
	if(Event != pygame.NOEVENT):
		if(Event == pygame.KEYDOWN):
		print(Event)
