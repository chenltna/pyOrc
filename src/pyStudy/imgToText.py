#coding=gbk
import cv2;
import json;
import pytesseract;
from pytesseract import Output;
from PIL import Image;
from PIL import ImageDraw;
from PIL import ImageFont;
import numpy as np;

'''
ʶ���ַ���������ʶ����ַ��ı���Ϣ
'''
shuzi = pytesseract.image_to_string(Image.open('resource/demo2.png'), lang='chi_sim');
print "��װ��Tesseract�汾:"
print pytesseract.get_tesseract_version()
print(shuzi)

def recoText(im):
    """
    ʶ���ַ���������ʶ����ַ������ǵ�����
    :param im: ��Ҫʶ���ͼƬ
    :return data: �ַ���������ͼƬ��λ��
    """
    data = {}
    d = pytesseract.image_to_data(im, output_type=Output.DICT, lang='chi_sim')
    for i in range(len(d['text'])):
        if 0 < len(d['text'][i]):
            (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
            data[d['text'][i]] = ([d['left'][i], d['top'][i], d['width'][i], d['height'][i]])
 
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 1)
            # ʹ��cv2.putText������ʾ���ģ���Ҫʹ������Ĵ������
            #cv2.putText(im, d['text'][i], (x, y-8), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (255, 0, 0), 1)
 
            pilimg = Image.fromarray(im)
            draw = ImageDraw.Draw(pilimg)
            # ����1�������ļ�·��������2�������С
            font = ImageFont.truetype("simhei.ttf", 15, encoding="gbk")
            # ����1����ӡ���꣬����2���ı�������3��������ɫ������4������
            draw.text((x, y-10), d['text'][i], (255, 0, 0), font=font)
            im = cv2.cvtColor(np.array(pilimg), cv2.COLOR_RGB2BGR)
 
    cv2.imshow("recoText", im)
    return data
 
if __name__ == '__main__':
    img = cv2.imread('resource/demo1.jpg')
    #cv2.imshow("src", img)
    data = recoText(img)
    print  data
 
    cv2.waitKey(0)
    cv2.destroyAllWindows()
