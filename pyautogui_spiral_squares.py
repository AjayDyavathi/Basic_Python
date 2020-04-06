# execute this program, then place your cursor on something like paint app, to draw spiral squares


import pyautogui
import time
print('place the cursor..')
time.sleep(2)
pyautogui.click()
distance = 200
t = 1
while distance > 0:
    pyautogui.dragRel(distance, 0, duration = t)
    distance = distance - 5
    pyautogui.dragRel(0, distance, duration = t)
    pyautogui.dragRel(-distance, 0, duration = t)
    distance = distance - 5
    pyautogui.dragRel(0, -distance, duration = t)
