# PycklePi
PycklePi is a small module for controlling buttons, LED's, buzzers and more on the Raspberry Pi 3. It uses the RPi.GPIO module and requires hardware along with it. 

## Help
You can find all help and documentation on the official PycklePi Github page. There are examples, documentation, and more to help beginners in starting with Raspberry Pi's and PycklePi. 

## Modules
#### Set's up the main information and sets the GPIO pins as BCM (Broadcom pin-numbering scheme)
PycklePi.setup()
#### Set's up a specified button to the GPIO pin passed as the argument
PycklePi.buttonSetup()
#### Set's up a specified LED to the GPIO pin passed as the argument
PycklePi.LEDSetup()
#### Set's up a specified buzzer to the GPIO pin passed as the argument
PycklePi.buzzerSetup()
#### Turns off the specified LED
PycklePi.LEDoff()
#### Turns on the specified LED
PycklePi.LEDon()
#### Flashes the specified LED for the amount of time specified
PycklePi.LEDon_flashing()
#### Buzzes the buzzer for the amount of time specified
PycklePi.buzzerOn_beeping()
#### Turns on the LED for the time specified
PycklePi.LEDon_timed()
#### When the specified button is pressed, it goes to the function passed as the argument
PycklePi.buttonPush()
#### When any of the specified button(s) are pressed, it goes to the function(s) passed as the argument
PycklePi.buttonPush2()
#### When any of the specified button(s) are pressed, it goes to the function(s) passed as the argument
PycklePi.buttonPush3()
#### Turns on the specified buzzer until turned off
PycklePi.buzzerOn()
#### Turns off the specified buzzer.
PycklePi.buzzerOff()
#### When the specified button is pressed, the specified LED is turned on for the amount of seconds set in the program
PycklePi.button_led()
#### When the specified button is pressed, the specified buzzer is turned on for the amount of seconds set in the program
PycklePi.button_buzzer()
#### Used at the end of a program, it "cleans" any used and unused ports/pins to make sure nothing is short-circuited
PycklePi.cleanup()
