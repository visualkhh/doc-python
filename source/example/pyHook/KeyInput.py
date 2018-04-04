import win32api


# Check the python tiler on github, very useful even if you are trying to just find key codes to send. Also this will be useful if you are running your code in the background and want to break the loop from outside the window.
# git project: https://github.com/Tzbob/python-windows-tiler
# code with windows keys: https://code.google.com/p/python-windows-tiler/source/browse/pwt/hotkey.py?r=df41af2a42b6304047a5f6f1f2903b601b22eb39

while True :
    cp = win32api.GetCursorPos()
    print(cp)
    if win32api.KeyPress('H') == True :
        break