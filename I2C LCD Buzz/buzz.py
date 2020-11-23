import random
import time
import I2C_LCD_driver

mylcd = I2C_LCD_driver.lcd()

# Define the list of Buzzwords
myList = ["Monkeys under the table", "Ducks in a row", "Teamwork makes the dream work", "Run it up the flag pole", "Bandwidth", "Fit for purpose", "Baked in"]

# Starting up the screen
mylcd.lcd_display_string("The Buzz-o-matic 3000", 1)
time.sleep(1)
mylcd.lcd_clear()

mylcd.lcd_display_string ("Press the button and I'll cover you in bullshit")
time.sleep(2)
mylcd.lcd_clear()

#Waiting for the button to be pressed

#Detected that the button has be pressed so carrying on with the script

mylcd.lcd_display_string ("Just thinking up some rubbish phrases")
time.sleep(2)
mylcd.lcd_clear()

mylcd.lcd_display_string ("Ready or not here it comes")
time.sleep(1)
mylcd.lcd_clear()
time.sleep(1)

#Displaying the phrase that needs to be said

mylcd.lcd_display_string (random.choice(myList))

#Going back through the loop and then waiting for the button to be pressed again
mylcd.lcd_display_string ("Shall we do it again? Just press the button for another")
