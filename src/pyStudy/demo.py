#coding=gbk

#��ά��
from claptcha import Claptcha
from PIL import Image
import pytesseract

im = Image.open('resource/demo1.jpg')
#��ֵ��ͼ����ͼ�����ֵ
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
#��ʾ��ֵ�������ĺڰ�ͼ��
image.show()

result=pytesseract.image_to_string(image,lang='chi_sim')
print(result)
