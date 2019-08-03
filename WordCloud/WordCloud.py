# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:45:14 2019

@author: ASUS
"""

import os
from wordcloud import WordCloud
import jieba
import PIL
import matplotlib.pyplot as plt
import numpy as np
import pdfplumber

def wordcloudplot(txt):
    path = 'C:/Windows/Fonts/simhei.ttf'
    #path = str(path,'utf8').encode('gb18030')
    
    '''
    词云背景图
    '''
    alice_mask = np.array(PIL.Image.open('E:\\PythonDataAnalysis\\WordCloud\\nwpu.jpg'))
    wordcloud = WordCloud(font_path=path,
                          background_color="white",
                          margin=5,width=1800,height=800,
                          mask=alice_mask,max_words=2000,
                          max_font_size=60,random_state=42,scale=5)
    wordcloud=wordcloud.generate(txt)
    
    '''
    所生成的词云图片
    '''
    wordcloud.to_file('E:\\PythonDataAnalysis\\WordCloud\\nwpu_wordcloud.jpg')
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    
def main():
    '''
    读取txt文件
    '''
#    a = []
#    f = open('E:\\PythonDataAnalysis\\a.txt','rb').read()
#    words = list(jieba.cut(f))
#    for word in words:
#        if len(word)>1:
#            a.append(word)
#    txt = ' '.join(a)
#    wordcloudplot(txt)
    
    '''
    读取pdf文件
    Path:pdf文件的路径
    tempFilePath:把pdf文件转换成txt文件，在用jieba.cut对txt文件中的内容进行切词。
                 其中，txt文件的路径就是tempFilePath   
    '''
    a = []
    Path = "E:\\PythonDataAnalysis\\WordCloud\\report.pdf"
    tempFilePath = 'E:\\PythonDataAnalysis\\WordCloud\\report.txt'
    f = open(tempFilePath,'a+',encoding='utf-8')
    f.seek(0)
    with pdfplumber.open(Path) as pdf:
        for page in pdf.pages:     
            f.write(page.extract_text())
    f.close()
    
    f = open(tempFilePath,'rb').read()
    words = list(jieba.cut(f))
    for word in words:
        if len(word)>1:
            a.append(word)
    txt = ' '.join(a)
    wordcloudplot(txt)
    
    if os.path.exists(tempFilePath):
        os.remove(tempFilePath)
            

if __name__=='__main__':
    main()    