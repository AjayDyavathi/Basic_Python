import pyautogui
x0, y0 = '', ''
print('''This program will display the position of cursor;
Press Ctrl + C to exit
Press ENTER to continue''')
input()
try:
    while True:
        x, y = pyautogui.position()
        if x0 != x and y0 != y:
            x0, y0 = x, y
            pixelColor = pyautogui.screenshot().getpixel((x, y))
            color = 'RGB : ({}, {}, {})'.format(str(pixelColor[0]).rjust(3), str(pixelColor[1]).rjust(3), str(pixelColor[2]).rjust(3))
            print('X : '+ str(x).rjust(4) + ', Y : ' + str(y).rjust(4) + ', ' + color)
            
except KeyboardInterrupt:
    print('Done')
