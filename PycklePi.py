import time
import RPi.GPIO as GPIO

def setup():
    try:
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
        GPIO.setwarnings(False)
    except Exception as e:
        print ("Error!")
        print (e)
    
def LEDSetup(LEDpin):
    try:
        GPIO.setup(LEDpin, GPIO.OUT) # LED pin set as output
    except Exception as e:
        print ("Error!")
        print (e)
        
def buttonSetup(butPin):
    try:
        GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    except Exception as e:
        print ("Error!")
        print (e)

def buzzerSetup(buzPin):
    try:
        GPIO.setup(buzPin, GPIO.OUT) # LED pin set as output
    except Exception as e:
        print ("Error!")
        print (e)

def LEDoff(LEDpin):
    try:
        GPIO.output(LEDpin, GPIO.LOW)
    except Exception as e:
        print ("Error!")
        print (e)

def LEDon(LEDpin):
    try:
        GPIO.output(LEDpin, GPIO.HIGH)
    except Exception as e:
        print ("Error!")
        print (e)

def LEDon_flashing(LEDpin, inter, flashes):
    try:
        for i in range(flashes):
            GPIO.output(LEDpin, GPIO.HIGH)
            time.sleep(inter)
            GPIO.output(LEDpin, GPIO.LOW)
            time.sleep(inter)
    except Exception as e:
        print ("Error!")
        print (e)

def buzzerOn_beeping(buzzerPin, inter, beeps):
    try:
        for i in range(beeps):
            GPIO.output(buzzerPin, GPIO.HIGH)
            time.sleep(inter)
            GPIO.output(buzzerPin, GPIO.LOW)
            time.sleep(inter)
    except Exception as e:
        print ("Error!")
        print (e)

def LEDon_timed(LEDpin, time):
    try:
        GPIO.output(LEDpin, GPIO.HIGH)
        time.sleep(time)
        GPIO.output(LEDpin, GPIO.LOW)
    except Exception as e:
        print ("Error!")
        print (e)
        
def buttonPush(butPin, whattosay):
    while True:
        try:
            if GPIO.input(butPin) == False:
                whattosay()
                time.sleep(0.08)
        except Exception as e:
            print ("Error!")
            print (e)

def buttonPush2(butPin, whattosay1, butPin1, whattosay):
    while True:
        input_state = GPIO.input(butPin)
        input_state1 = GPIO.input(butPin1)
        if input_state == False:
            whattosay1()
            time.sleep(0.08)
        if input_state1 == False:
            whattosay()
            time.sleep(0.08)

def buttonPush3(butPin, whattosay1, butPin1, whattosay2, butPin2, whattosay):
    while True:
        try:
            input_state = GPIO.input(butPin)
            input_state1 = GPIO.input(butPin1)
            input_state2 = GPIO.input(butPin2)
            if input_state == False:
                whattosay1()
                time.sleep(0.08)
            if input_state1 == False:
                whattosay2()
                time.sleep(0.08)
            if input_state2 == False:
                whattosay()
                time.sleep(0.08)
        except Exception as e:
            print ("Error!")
            print (e)

def buzzerOn(buzPin):
    try:
        GPIO.output(buzPin, GPIO.HIGH)
    except Exception as e:
        print ("Error!")
        print (e)
        GPIO.output(buzPin, GPIO.LOW)
        
def buzzerOff(buzPin):
    try:
        GPIO.output(buzPin, GPIO.LOW)
    except Exception as e:
        print ("Error!")
        print (e)

def button_led(butPin, LEDpin, secs):
    while True:
        try:
            if GPIO.input(butPin) == False:
                GPIO.output(LEDpin, GPIO.HIGH)
                time.sleep(secs)
                GPIO.output(LEDpin, GPIO.LOW)
        except Exception as e:
            print ("Error!")
            print (e)

def button_buzzer(butPin, buzPin, secs):
    while True:
        try:
            if GPIO.input(butPin) == False:
                GPIO.output(buzPin, GPIO.HIGH)
                time.sleep(secs)
                GPIO.output(buzPin, GPIO.LOW)
        except Exception as e:
            print ("Error!")
            print (e)

def cleanup():
    try:
        GPIO.cleanup()
    except Exception as e:
        print ("Error!")
        print (e)
