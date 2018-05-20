#!/usr/bin/python
# -*- coding:utf-8 -*-

from datetime import datetime
import itchat
from itchat.content import *
import os
import time

 
@itchat.msg_register([TEXT,PICTURE, RECORDING, ATTACHMENT, VIDEO])
def SentChatRoomsMsg(imgname,img):
    #rooms = itchat.get_chatrooms(update=True)
    group1 = itchat.search_chatrooms(name=u"购物福利券群")
    group2 = itchat.search_chatrooms(name=u"淘宝优惠券")
    #lp = itchat.search_friends(name=u"老婆")
    sendto(group1,imgname,img)
    sendto(group2,imgname,img)
    #sendto(lp,imgname,img)
    
@itchat.msg_register([TEXT,PICTURE, RECORDING, ATTACHMENT, VIDEO])
def sendto(allname,imgname,img):
    userName = allname[0]['UserName']
    nickname = allname[0]['NickName']
    itchat.send_image(img, userName)
    #itchat.send_msg('hello',userName)
    print("发送到：" + nickname + "\n"+"发送内容：" + imgname + "\n")

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

def loginCallback():
    print("***登录成功***")


def exitCallback():
    print("***已退出***")

if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=True, loginCallback=loginCallback, exitCallback=exitCallback)
    dirpath = mkDir("图片")
    imagedic = getimage(dirpath)
    #print (imagedic)
    try :
        for key,value in imagedic.items():
            true_value = value.replace('\\','/')
            print (key+":"+true_value)
            SentChatRoomsMsg(key,true_value)
            time.sleep(300)
    except KeyboardInterrupt:
        print('暂停一下')
    finally:
        itchat.dump_login_status()