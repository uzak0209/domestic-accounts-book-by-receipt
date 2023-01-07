import pyocr
from PIL import Image, ImageEnhance
import os
import re
def identify():
    #Pah設定
    TESSERACT_PATH = "C:\\Program Files\\Tesseract-OCR" #インストールしたTesseract-OCRのpath
    TESSDATA_PATH = 'C:\Program Files\\Tesseract-OCR\\tessdata' #tessdataのpath
    
    os.environ["PATH"] += os.pathsep + TESSERACT_PATH
    os.environ["TESSDATA_PREFIX"] = TESSDATA_PATH
    
    #OCRエンジン取得;
    
    
    tools = pyocr.get_available_tools()
    print(tools[0].get_name())
    tool = tools[0]
    
    #OCR対象の画像ファイルを読み込む
    img = Image.open("final.jpg")
    
    
    #画像を読みやすいように加工。
    img=img.convert('RGB')
    size=img.size
    img2=Image.new('RGB',size)
    
    border=400
    
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b=img.getpixel((x,y))
            if r > border or g > border or b > border:
                r = 255
                g = 255
                b = 255
            img2.putpixel((x,y),(r,g,b))
    img2.show()
    
    #画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    text = tool.image_to_string(img2, lang="jpn", builder=builder)
   
    y=""
    for x in text:
        if x=="①":
            x=1
        elif x == "②":
            x=2
        elif x == "③":
            x=3
        elif x == "④":
            x=4
        elif x=="⑤":
                x=5
        elif x == "⑥":
            x=6
        elif x == "⑦":
            x=7
        elif x == "⑧":
            x=8
        elif x=="⑨":
            x=9
        elif x=="⑩":
            x=10
        elif x=="⑪":
            x=11
        elif x == "⑫":
            x=12
        elif x == "⑬":
            x=13
        elif x == "⑭":
            x=14
        elif x=="⑮":
            x=15
        elif x == "⑯":
            x=16
        elif x == "⑰":
            x=17
        elif x == "⑱":
            x=18
        elif x=="⑲":
            x=19
        elif x=="⑳":
            x=20
        y=y+str(x)
    
    text=y
    print(text)

    status=0
    separated_list = re.split("[\n ]",text)
    final_list=[]
    a=0
    i=0
    first=0
    for word in separated_list:
        
        if(len(word) ==0):
            pass
        
        elif(word[0]=="\\"):
            if(first==0):
                final_list=[]
                final_list.append(str(reword))
                first=first+1
                i=1
                a=0
            word=word.replace("\\","")
            final_list.append(str(word))
            i=i+1
            status=0

        
        elif status == 1 and str.isdigit(word)==False:
        
            x=final_list.pop(i-1+a)
            word_s=str(x)+str(word)
            if "小計" in word_s or "合計" in word_s:
                break
            final_list.append(str(word_s))
            reword=word_s
            
            
        else:
            final_list.append(word)
            i=i+1
            status=1
            reword=word
    status = 1
    final1_list=[]
    tmp_tuple=()
    print(final_list)
    for word in final_list:
        if status == 1:
            back_word = word
            status = 0
        elif status == 0:
            tmp_tuple=(back_word,word)
            final1_list.append(tmp_tuple)
            status = 1
    print(final1_list)
    return final1_list


    
  


            
