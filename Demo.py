import Detect
import PIL.Image
import PIL.ImageOps
a = ''
c = ''
'''
while True:
    print('請輸入一待測數字: (0~9)')
    num=input()
    print('請輸入樣本編號  Page00xx(2位數)')
    no=input()
    data = PIL.Image.open('./test/'+str(num)+'/Page00'+str(no)+'.jpg')
    data.show()
    invert = PIL.ImageOps.invert(data) 
    a,c = Detect.DetectAPic(invert)
    print('電腦認為此數字為:',a,'機率為:',c,'%')
'''
data1 = PIL.Image.open('./test/1.jpg') 
invert1 = PIL.ImageOps.invert(data1) 
a,c = Detect.DetectAPic(invert1)
print('test/1.jpg','預測結果:',a,'信心指數:',c)

data2 = PIL.Image.open('./test/2.jpg') 
invert2 = PIL.ImageOps.invert(data2) 
a,c = Detect.DetectAPic(invert2)
print('test/2.jpg','預測結果:',a,'信心指數:',c)


data3 = PIL.Image.open('./test/3.jpg') 
invert3 = PIL.ImageOps.invert(data3) 
a,c = Detect.DetectAPic(invert3)
print('test/3.jpg','預測結果:',a,'信心指數:',c)

data4 = PIL.Image.open('./test/4.jpg') 
invert4 = PIL.ImageOps.invert(data4) 
a,c = Detect.DetectAPic(invert4)
print('test/4.jpg','預測結果:',a,'信心指數:',c)

data5 = PIL.Image.open('./test/5.jpg') 
invert5 = PIL.ImageOps.invert(data5) 
a,c = Detect.DetectAPic(invert5)
print('test/5.jpg','預測結果:',a,'信心指數:',c)

data6 = PIL.Image.open('./test/6.jpg') 
invert6 = PIL.ImageOps.invert(data6) 
a,c = Detect.DetectAPic(invert6)
print('test/6.jpg','預測結果:',a,'信心指數:',c)

data7 = PIL.Image.open('./test/7.jpg') 
invert7 = PIL.ImageOps.invert(data7) 
a,c = Detect.DetectAPic(invert7)
print('test/7.jpg','預測結果:',a,'信心指數:',c)

data8 = PIL.Image.open('./test/8.jpg') 
invert8 = PIL.ImageOps.invert(data8) 
a,c = Detect.DetectAPic(invert8)
print('test/8.jpg','預測結果:',a,'信心指數:',c)

data9 = PIL.Image.open('./test/9.jpg') 
invert9 = PIL.ImageOps.invert(data9) 
a,c = Detect.DetectAPic(invert9)
print('test/9.jpg','預測結果:',a,'信心指數:',c)

data10 = PIL.Image.open('./test/10.jpg') 
invert10 = PIL.ImageOps.invert(data10) 
a,c = Detect.DetectAPic(invert10)
print('test/10.jpg','預測結果:',a,'信心指數:',c)

