from PIL import Image, ImageDraw, ImageFont, ImageFilter



goods_img = Image.open('longpic12382207119.jpg')

goods_img_w, goods_img_h = goods_img.size


Last_Image = Image.new('RGB',(goods_img_w,goods_img_h+340),'white')
loc1 = (0,0)
Last_Image.paste(goods_img, loc1)
Qr_Image = Image.open('qr12382207119.jpg')
loc2 = (0,goods_img_h)
Last_Image.paste(Qr_Image, loc2)

font1 = ImageFont.load_default()
font2 = ImageFont.truetype(r'data/msyh.ttf', 28)
font3 = ImageFont.truetype(r'data/msyh.ttf', 28)

draw = ImageDraw.Draw(Last_Image)

Last_Image_w, Last_Image_h = Last_Image.size

draw.text((370,goods_img_h),text='原价:39元   现价:1元',font=ImageFont.load_default().font,fill='red')

s='选用高档丝光棉面料，亲肤柔软，透气舒适，休闲简约版型，中老年男士百搭单品，父爱如山，送爸爸一件透气凉爽的POLO衫。【赠运费险】'
draw.text((340,goods_img_h+80),text='\n'.join(s[i:i+15] for i in range(0,len(s),15)),font=font2,fill='black')

draw.text((50,Last_Image_h-40),text='长按识别二维码',font=font3,fill='red')

Last_Image.save('merged.jpg')