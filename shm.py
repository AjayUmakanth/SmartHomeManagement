from flask import Flask 
from flask_ask import Ask, statement, convert_errors 
import RPi.GPIO as GPIO 
import logging 

GPIO.setmode(GPIO.BOARD) 
app = Flask(__name__) 
ask = Ask(app, '/') 
logging.getLogger("flask_ask").setLevel(logging.DEBUG) 

currentRoom="living"

#Lift r33, g35, b37
lift1=33 
lift2=35 
lift3=37

#door 32
door=32

#garden 24
sprinkler=24

#--living room-- fan 12
livingfan=12

#curtain 40
livingcurtain=40

#light 29 
livinglight=29

#tv 31
livingtv=31

#--kitchen-- light 26
kitchenlight=26

#coffee 23
kitchencoffee=23

#--bedroom-- ac 20
bedroomac=18

#light 21
bedroomlight=21

#turn {device} {status}
@ask.intent('SHMMainIntent', mapping={'status': 'status', 'device': 'device'}) 
def shm_main_control(status, device):
	try:
		deviceName=str(device)
		statusName =str(status)
		print(deviceName)
	except Exception as e:
        	print(e)
	
	if deviceName == 'TV' :
		if currentRoom == 'living':
			if statusName=='on':
				GPIO.setup(livingtv, GPIO.IN)
				if GPIO.input(livingtv)==True:
					return statement('TV is already on')
				else:
					GPIO.setup(livingtv, GPIO.OUT)
					GPIO.output(livingtv,GPIO.HIGH)
					return statement('TV is on')
			elif statusName=='off' :
				GPIO.setup(livingtv, GPIO.IN)
				if GPIO.input(livingtv)==False:
					return statement('TV is already off')
				else:
					GPIO.setup(livingtv, GPIO.OUT)
					GPIO.output(livingtv,GPIO.LOW)
					return statement('TV is off')
			else:
				return statement('Invalid input')
		else:
			return statement('Invalid input')
	#----------------------------------------------------------------
	elif deviceName == 'fan':
		if currentRoom == 'living' :
			if statusName=='on':
				GPIO.setup(livingfan, GPIO.IN)
				if GPIO.input(livingfan)==True:
					return statement('Fan is already on')
				else:
					GPIO.setup(livingfan, GPIO.OUT)
					GPIO.output(livingfan,GPIO.HIGH)
					return statement('Fan is on')
			elif statusName=='off' :
				GPIO.setup(livingfan, GPIO.IN)
				if GPIO.input(livingfan)==False:
					return statement('Fan is already off')
				else:
					GPIO.setup(livingfan, GPIO.OUT)
					GPIO.output(livingfan,GPIO.LOW)
					return statement('Fan is off')
			else:
				return statement('Invalid input')
		else:
			return statement('Invalid input')
	#-----------------------------------------------------------------
	elif deviceName == 'light':
		if currentRoom == 'living':
			if statusName=='on':
				GPIO.setup(livinglight, GPIO.IN)
				if GPIO.input(livinglight)==True:
					return statement('Light is already on')
				else:
					GPIO.setup(livinglight, GPIO.OUT)
					GPIO.output(livinglight,GPIO.HIGH)
					return statement('Light is on')
			elif statusName=='off' :
				GPIO.setup(livinglight, GPIO.IN)
				if GPIO.input(livinglight)==False:
					return statement('Light is already off')
				else:
					GPIO.setup(livinglight, GPIO.OUT)
					GPIO.output(livinglight,GPIO.LOW)
					return statement('Light is off')
			else:
				return statement('Invalid input')
		elif currentRoom == 'bed':
			if statusName=='on':
				GPIO.setup(bedroomlight, GPIO.IN)
				if GPIO.input(bedroomlight)==True:
					return statement('Light is already on')
				else:
					GPIO.setup(bedroomlight)
					GPIO.output(bedroomlight)
					return statement('Light is on')
			elif statusName=='off' :
				GPIO.setup(bedroomlight, GPIO.IN)
				if GPIO.input(bedroomlight)==False:
					return statement('Light is already off')
				else:
					GPIO.setup(bedroomlight, GPIO.OUT)
					GPIO.output(bedroomlight,GPIO.LOW)
					return statement('Light is off')
			else:
				return statement('Invalid input')
		elif currentRoom == 'kitchen':
			if statusName=='on':
				GPIO.setup(kitchenlight, GPIO.IN)
				if GPIO.input(kitchenlight)==True:
					return statement('Light is already on')
				else:
					GPIO.setup(kitchenlight, GPIO.OUT)
					GPIO.output(kitchenlight,GPIO.HIGH)
					return statement('Light is on')
			elif statusName=='off' :
				GPIO.setup(kitchenlight, GPIO.IN)
				if GPIO.input(kitchenlight)==False:
					return statement('Light is already off')
				else:
					GPIO.setup(kitchenlight, GPIO.OUT)
					GPIO.output(kitchenlight,GPIO.LOW)
					return statement('Light is off')
			else:
				return statement('Invalid input')
		else:
			return statement('Invalid input')
	#-------------------------------------------------------------
	elif deviceName == 'AC':
		if(currentRoom == 'bedroom'):
			if statusName=='on':
				GPIO.setup(bedroomac, GPIO.IN)
				if GPIO.input(bedroomac)==True:
					return statement('AC is already on')
				else:
					GPIO.setup(bedroomac, GPIO.OUT)
					GPIO.output(bedroomac,GPIO.HIGH)
					return statement('AC is on')
			elif statusName=='off' :
				GPIO.setup(bedroomac, GPIO.IN)
				if GPIO.input(bedroomac)==False:
					return statement('AC is already off')
				else:
					GPIO.setup(bedroomac, GPIO.OUT)
					GPIO.output(bedroomac,GPIO.LOW)
					return statement('AC is off')
			else:
				return statement('Invalid input')
		else:
			return statement('Invalid input')
	#-------------------------------------------------------------
	elif deviceName == 'sprinkler':
		if statusName=='on':
			GPIO.setup(sprinkler, GPIO.IN)
			if GPIO.input(sprinkler)==True:
				return statement('Sprinkler is already on')
			else:
				GPIO.setup(sprinkler, GPIO.OUT)
				GPIO.output(sprinkler,GPIO.HIGH)
				return statement('Sprinkler is on')
		elif statusName=='off' :
			GPIO.setup(sprinkler, GPIO.IN)
			if GPIO.input(sprinkler)==False:
				return statement('Sprinkler is already off')
			else:
				GPIO.setup(sprinkler, GPIO.OUT)
				GPIO.output(sprinkler,GPIO.LOW)
				return statement('Sprinkler is off')
		else:
			return statement('Invalid input')
	#-------------------------------------------------------------
	elif deviceName == 'coffee':
		if currentRoom == 'kitchen':
			if statusName=='on':
				GPIO.setup(kitchencoffee, GPIO.IN)
				if GPIO.input(kitchencoffee)==True:
					return statement('Coffee is already on')
				else:
					GPIO.setup(kitchencoffee, GPIO.OUT)
					GPIO.output(kitchencoffee,GPIO.HIGH)
					return statement('Coffee is on')
			elif statusName=='off' :
				GPIO.setup(kitchencoffee, GPIO.IN)
				if GPIO.input(kitchencoffee)==False:
					return statement('Coffee is already off')
				else:
					GPIO.setup(kitchencoffee, GPIO.OUT)
					GPIO.output(kitchencoffee,GPIO.LOW)
					return statement('Coffee is off')
			else:
				return statement('Invalid input')
		else:
			return statement('Invalid input')
	
	#-------------------------------------------------------------
	elif deviceName == 'power':#turns of all light
		if statusName=='on':
			GPIO.setup(kitchenlight, GPIO.OUT)
			GPIO.output(kitchenlight,GPIO.HIGH)
			GPIO.setup(bedroomlight, GPIO.OUT)
			GPIO.output(bedroomlight,GPIO.HIGH)
			GPIO.setup(livinglight, GPIO.OUT)
			GPIO.output(livinglight,GPIO.HIGH)
			return statement('Turned on all lights')

		elif statusName=='off' :
			GPIO.setup(kitchenlight, GPIO.OUT)
			GPIO.output(kitchenlight,GPIO.LOW)
			GPIO.setup(bedroomlight, GPIO.OUT)
			GPIO.output(bedroomlight,GPIO.LOW)
			GPIO.setup(livinglight, GPIO.OUT)
			GPIO.output(livinglight,GPIO.LOW)
			return statement('Turned off all lights')

			
		else:
			return statement('Invalid input')
	return statement('Invalid input')
	
#switch to {room} room
@ask.intent('SHMRoomIntent', mapping={'room': 'room'}) 
def shm_change_room(room):
	try:
		roomName=str(room)
		currentRoom=roomName
		print(roomName)
				
	except Exception as e:
        	print(e)
	
	if roomName=='living' or  roomName=='bed' or roomName=='kitchen' :
		return statement('Switched to {}'.format(room))
		
	else:
		return statement('Invalid input')
	
#{status} house
@ask.intent('SHMLockIntent', mapping={'lockstatus': 'lockstatus'}) 
def shm_lock(lockstatus):
	try:
		statusName=str(status)
	except Exception as e:
        return statement('Invalid input')
		
	if statusName == 'lock':#turns of all light
		GPIO.setup(door, GPIO.IN)
		if GPIO.input(door)==True:
			return statement('Door is already locked')
		else:
			GPIO.setup(door, GPIO.OUT)
			GPIO.output(door,GPIO.HIGH)
			return statement('Door is locked')
	elif statusName=='unlock' :
		GPIO.setup(door, GPIO.IN)
		if GPIO.input(door)==False:
			return statement('Door is already unlocked')
		else:
			GPIO.setup(door)
			GPIO.output(door,GPIO.LOW)
			return statement('Door is unlocked')
	else:
		return statement('Invalid input')


if __name__ == '__main__':
	port = 5000 #the custom port you want
	app.run(host='0.0.0.0', port=port)
