# encoding=utf8
import pandas as pd
import qrcode
from  PIL import Image
from  PIL import ImageDraw
from  PIL import ImageFont

url = r"D:\E Disk\Python\QR\20180126\QR new 20180126.csv" #CHANGE
tips= pd.read_csv(url,encoding="utf-8")
pd.set_option('max_colwidth',10000)
df1=tips

def  make_qr(url,pos,name):
     qr = qrcode.QRCode(
        version=4,  # 生成二维码尺寸的大小 1-40  1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M,  # L:7% M:15% Q:25% H:30%
        box_size=10,  # 每个格子的像素大小
        border=4,  # 边框的格子宽度大小
    )
     qr.add_data(url)
     qr.make(fit=True)
     img = qr.make_image()
     #img = qrcode.make(url)
     text=str(pos)+"_"+str(name)
     a="D:/E Disk/Python/QR/20180126/" #CHANGE
     b= '.png'
     fl= a+text +b
     img.save(fl, quality=100)
     # 设置所使用的字体
     font = ImageFont.truetype("C:\Windows\Fonts\Arial.ttf", 24)
     # 打开图片
     imageFile = fl
     im1 = Image.open(imageFile)
     # 画图
     draw = ImageDraw.Draw(im1)
     draw.text((180, 15), str(pos), font=font)  # 设置文字位置/内容/颜色/字体
     draw = ImageDraw.Draw(im1)
     im1.save(fl, quality=100)

df1.apply(lambda x: make_qr(x['TEXT_URL'],x['CODE_SALESROOM'],x['NAME_SALESROOM']),axis=1)
