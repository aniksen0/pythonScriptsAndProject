#this script will input number (serially) in the form! 

import pyautogui



i=int(input("enter"))

for x in range(14,i):
    print(x)
    d=str(x)
    pyautogui.typewrite(d)
    pyautogui.press('enter')
    pyautogui.sleep(0.200)
   
  