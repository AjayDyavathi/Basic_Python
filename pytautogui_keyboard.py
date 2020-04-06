import pyautogui
import time
time.sleep(2)
pyautogui.click()
pyautogui.typewrite('Hello world!')
pyautogui.typewrite('\nHi AJAY\n', 0.25)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])

pyautogui.keyDown('shift'); pyautogui.press('4'); pyautogui.keyUp('shift')

pyautogui.hotkey('shift', '5')




