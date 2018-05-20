#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os 
import time
import win32api
import win32gui
import win32con
import win32clipboard as win32clipboard

from ctypes import *  
from PIL import Image  



def setImage(aString):

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_BITMAP, aString)
    win32clipboard.CloseClipboard()

def send_wechat(msg):

    setImage(msg)
    wechat = win32gui.FindWindow('ChatWnd', u"购物福利券群")
    win32gui.SetForegroundWindow(wechat)
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(86,0,0,0)
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)  
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) 
    win32gui.SetWindowPos(wechat, win32con.HWND_BOTTOM, 0, 0, 0, 0,win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
    wechat2 = win32gui.FindWindow('ChatWnd', u"淘宝优惠券")
    win32gui.SetForegroundWindow(wechat2)
    win32api.keybd_event(17,0,0,0)
    win32api.keybd_event(86,0,0,0)
    win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0)  
    win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
    win32api.keybd_event(13,0,0,0)
    win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) 
    win32gui.SetWindowPos(wechat2, win32con.HWND_BOTTOM, 0, 0, 0, 0,win32con.SWP_NOSIZE | win32con.SWP_NOMOVE)
def mkDir(dirName):
    aa = os.getcwd()
    dirpath = os.path.join(aa, dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath

def getimage(file_dir):   
    images = {}
    for root, dirs, files in os.walk(file_dir):  
        for name in files:
            images[name] = os.path.join(root,name)
    return images
if __name__ == '__main__':

    dirpath = mkDir("图片")
    imagedic = getimage(dirpath)
    #print (imagedic)
    try :
        for key,value in imagedic.items():
            true_value = value.replace('\\','/')
            im = Image.open(true_value)  
            im.save('Temp.bmp')  
            msg = windll.user32.LoadImageW(0, "Temp.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)
            if msg != 0:
                send_wechat(msg)
            print (key+":"+true_value)
            time.sleep(10)
    except KeyboardInterrupt:
        print('暂停一下')

    
