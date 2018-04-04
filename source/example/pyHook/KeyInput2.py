# -*- coding: utf-8 -*-

import win32api,time,win32con


def keyb(ch=None,shift=False,control=False,alt=False, delaik=0.02):
    for b in ch:
        c=b
        if (b>='A' and b<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
        if b>='a' and b<='z':
            c=b.upper()
        if alt:
            win32api.keybd_event(win32con.VK_MENU, 0, 0, 0)
            time.sleep(0.250)
        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        if isinstance(b,(int)):
            cord=b
        else:
            cord=ord(c)

        win32api.keybd_event(cord, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
        if delaik>0.0:
            time.sleep(delaik)
        win32api.keybd_event(cord, 0, win32con.KEYEVENTF_EXTENDEDKEY |
                             win32con.KEYEVENTF_KEYUP, 0)
        if delaik>0.0:
            time.sleep(delaik)

        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0,
                                 win32con.KEYEVENTF_KEYUP, 0)
        if alt:
            win32api.keybd_event(win32con.VK_MENU, 0,
                                 win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.05)
        if (b>='A' and b<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0,
                                 win32con.KEYEVENTF_KEYUP, 0)



time.sleep(5)  #user has 5 sec for prepare a target-window
keyb("AZERTYUIOP ")
keyb("azertyuiop")
keyb("\r")
keyb("1234567890", shift=True) #shift == True for french keyboard
keyb("\n")
keyb("AAAAAAAAA\n")
time.sleep(1)
keyb("f", alt=True)  # {Alt} F   (ouvre menu ?)
time.sleep(1)
keyb([27,27])  # 2 x {Escape}