#coding=gbk

#二维码
from claptcha import Claptcha
from PIL import Image
import pytesseract

im = Image.open('resource/demo1.jpg')
#二值化图像传入图像和阈值
def erzhihua(image,threshold):
    ''':type image:Image.Image'''
    image=image.convert('L')
    table=[]
    for i in range(256):
        if i <  threshold:
            table.append(0)
        else:
            table.append(1)
    return image.point(table,'1')


image=erzhihua(im,127)
#显示二值化处理后的黑白图像
image.show()

result=pytesseract.image_to_string(image,lang='chi_sim')
print(result)
