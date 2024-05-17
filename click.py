import keyboard
import mouse
import time
from plyer import notification

# displaying a notification when the clicker is turned on or off
def show(title, message):
    notification.notify(title=title,
                        message=message,
                        app_icon='img.ico',
                        timeout=10)

Click = False 

# activating or deactivating the clicker
def clicker():
    global Click
    Click = not Click
    if Click:
        show('Clicker', 'The clicker is running')
    else:
        show('Clicker', 'The clicker is turned off')


keyboard.add_hotkey('O + P', clicker) # adding a keyboard shortcut to turn the clicker on and off

# clicks if the clicker is enabled
while True:
    if Click: 
        mouse.click(button='left') # mouse button
        time.sleep(0.1) # click delay