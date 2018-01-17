# -*-coding:utf-8 -*-
# __author__=coco
#处理图片基础操作

from PIL import Image

im = Image.open('westbrook.jpg','r')
size = im.size
for i in range(0,size[0]):
    for j in range(0,size[1]):
        old = im.getpixel((i,j))
        im.putpixel((i,j),(int(old[0]/2),int(old[1]/2),int(old[2]/2)))
im.show()
im.save("answer.jpg")