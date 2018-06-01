#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Author —— 李博

import re
import os
import time
import requests
import json  
import qrcode
import sys
import shutil
import threading
import random

from PIL import Image, ImageDraw, ImageFont
from pyquery import PyQuery as pq
pid = 'your alibaba pid'
appkey = 'your appkey'


        
def get_top_day_goods():

    getgoods_url = "http://api.taokezhushou.com/api/v1/top_day?app_key="+appkey
    getgoodsheaders = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "******************************************************************************************************",
        'cache-control': "no-cache",
        'postman-token': "8adf62ba-2f6f-4ecb-1870-082d14856c17"
        }
    response = requests.request("GET", getgoods_url, headers=getgoodsheaders)
    goods = response.json()
    goodslist = []
    for i in goods['data']:
        print (i['coupon_end_time'])
        goodslist.append(i['goods_id'])
    return goodslist

def get_top_hour_goods():

    getgoods_url = "http://api.taokezhushou.com/api/v1/top_hour?app_key="+appkey
    getgoodsheaders = {
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "******************************************************************************************************",
        'cache-control': "no-cache",
        'postman-token': "512b1baa-1e8a-c760-726b-6a722426601c"
        }
    response = requests.request("GET", getgoods_url, headers=getgoodsheaders)
    goods = response.json()
    goodslist = []
    for i in goods['data']:
        goodslist.append(i['goods_id'])
    return goodslist

def generate_img(good):

    #获取商品信息
    spurl = "http://www.taokezhushou.com/detail/"+str(good)
    spheaders = {
        'connection': "keep-alive",
        'cache-control': "no-cache",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'referer': "http://www.taokezhushou.com/",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "******************************************************************************************************",
        'postman-token': "8c3422c5-9403-7e03-18ef-48ec91cff0e7"
        }
    response = requests.request("GET", spurl, headers=spheaders)
    doc = pq(response.text)
    #print(doc('.resultpage'))
    #print(type(doc('#detail')))
    # print(response.text)
    # with open('explore.txt', 'a', encoding='utf-8') as f:
        # f.write(doc('.resultpage'))
    r = re.findall(r'var id = ([\s\S]+?)var goodsInfo', response.text, re.M)
    a = ''.join(r)
    b = re.compile('"+.*"?')
    result = b.findall(a)
    results = ''.join(result)
    results = results.replace('"','')
    results = results.replace(';','\n')
    results = results.split('\n') 
    name = ['id','goods_id','shop_type','goods_pic','goods_long_pic','goods_short_title_text','last_price','goods_price','goods_intro','goods_sale_num','coupon_amount','coupon_type','goods_link','seller_id','coupon_id']
    dic = dict(zip(name,results))
    print (dic)
    # print(dic['coupon_amount'])
    #获取qrid
    aliurl = "http://www.taokezhushou.com/alimama"
    alipayload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"goods_id\"\r\n\r\n"+dic['goods_id']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"coupon_id\"\r\n\r\n"+dic['coupon_id']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"text\"\r\n\r\n"+dic['goods_short_title_text']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"logo\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"pid\"\r\n\r\n"+pid+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"resp\"\r\n\r\nqr\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"goods_pic\"\r\n\r\n"+dic['goods_pic']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"shop_type\"\r\n\r\n"+dic['shop_type']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"goods_short_title\"\r\n\r\n"+dic['goods_short_title_text']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"last_price\"\r\n\r\n"+dic['last_price']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"goods_price\"\r\n\r\n"+dic['goods_price']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"goods_sale_num\"\r\n\r\n"+dic['goods_sale_num']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"coupon_amount\"\r\n\r\n"+dic['coupon_amount']+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    
    aliheaders = {
        'accept': "application/json, text/javascript, */*; q=0.01",
        'origin': "http://www.taokezhushou.com",
        'x-csrf-token': "3Q03Y9ONl0HDxL13Hyv87yW8iU03gvQLwOiW7ppy",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'dnt': "1",
        'referer': "http://www.taokezhushou.com/detail/527227835390",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9",
        'cookie': "******************************************************************************************************",
        'cache-control': "no-cache",
        'postman-token': "91cec8a2-ca45-379c-8804-40ec579f3f9a"
        }
    response = requests.request("POST", aliurl, data=alipayload.encode('utf-8'), headers=aliheaders)
    result = response.text
    result = json.loads(result) 
    # print (result)
    # print(type(result))
    # print (result["status"])
    # status = result["status"]
    # if status == 200:
        # qrcod = result["data"]["qrid"]
        # print (qrcod)
    dirpath = mkDir("图片")
    #################################生成二维码
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=1,
    )
    qr.add_data(result["data"]["qrlink"])
    qr.make(fit=True)
    QrImage = qr.make_image(fill_color="black", back_color="white")
    Qrname = os.path.join(dirpath,'qr')
    QrImage.save(Qrname+dic['goods_id']+'.jpg') 
    #################################生成长图
    goodsurl = dic['goods_long_pic']
    response = requests.get(goodsurl)
    goodsimg = response.content
    goodsname = os.path.join(dirpath,'long')
    with open(goodsname+dic['goods_id']+'.jpg','wb' ) as f:
        f.write(goodsimg)
        
    ##################################合成图片
    good_simg = Image.open(goodsname+dic['goods_id']+'.jpg')
    goods_img_w, goods_img_h = good_simg.size
    if goods_img_w < 800:
        goods_img_w = 800
    Last_Image = Image.new('RGB',(goods_img_w,goods_img_h+340),'white')
    loc1 = (0,0)
    Last_Image.paste(good_simg, loc1)
    Qr_Image = Image.open(Qrname+dic['goods_id']+'.jpg')
    loc2 = (0,goods_img_h)
    Last_Image.paste(Qr_Image, loc2)
    font1 = ImageFont.truetype(r'data/msyhbd.ttf', 32)
    font2 = ImageFont.truetype(r'data/msyh.ttf', 28)
    font3 = ImageFont.truetype(r'data/msyh.ttf', 28)
    draw = ImageDraw.Draw(Last_Image)
    Last_Image_w, Last_Image_h = Last_Image.size
    draw.text((370,goods_img_h),text='原价:'+dic['goods_price']+'元''   ''现价:'+dic['last_price']+'元',font=font1,fill='red')
    info=dic['goods_intro']
    draw.text((340,goods_img_h+80),text='\n'.join(info[i:i+15] for i in range(0,len(info),15)),font=font2,fill='black')
    draw.text((50,Last_Image_h-40),text='长按识别二维码',font=font3,fill='red')
    rstr = r"[\/\\\:\*\?\"\<\>\|]"
    title = re.sub(rstr, "_", dic['goods_short_title_text'])
    titlename = os.path.join(dirpath,title)
    Last_Image.save(titlename+'.jpg')
    print (title+'已生成')
    os.remove(goodsname+dic['goods_id']+'.jpg')
    os.remove(Qrname+dic['goods_id']+'.jpg')

def top_day():
    goods = get_top_day_goods()
    for good in goods:
        generate_img(good)

def top_hours():
    
    goods = get_top_hour_goods()
    for good in goods:
        try:
            generate_img(good)
        except:
            continue
def mkDir(dirName):
    aa = os.getcwd()
    dirpath = os.path.join(aa, dirName)
    if not os.path.exists(dirpath):
        os.mkdir(dirpath)
    return dirpath
        
if __name__ == "__main__":
    path = os.getcwd()
    path = os.path.join(path, '图片')
    shutil.rmtree(path)
    top_hours()
    top_day()
    generate_img('41352278982')
