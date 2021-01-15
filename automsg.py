import pyautogui
import random
count=0
#This script created for wishing my friends on there birthday.
gali=['deleted','deleted']

while count<100:
	pyautogui.sleep(2)
	pyautogui.typewrite("anything" +gali[random.randint(0,1)]+"happy birthday")
	pyautogui.press('enter')
print("{} msg sent".format(count))

