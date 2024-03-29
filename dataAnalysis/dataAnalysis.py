# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 16:13:11 2019

@author: ASUS
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#把json数据转换成DataFrame数据便于进行数据分析
def json_to_frame(jsonData):
    
    list_suoshuxiaoqu = []
    list_fangwuhuxing = []
    list_fangwudanjia = []
    list_suozaiweizhi = []
    list_jianzhumianji = []
    list_cankaoshoufu = []
    list_jianzaoniandai = []
    list_fangwuchaoxiang = []
    list_fangwuleixing = []
    list_suozailouceng = []
    list_zhuangxiuchengdu = []
    list_chanquannianxian = []
    list_peitaodianti = []
    list_fangbennianxian = []
    list_chanquanxingzhi = []
    list_peitaogongnuan = []
    list_weiyizhufang = []
    list_yishoufangyuan = []
    
    for i in range(len(jsonData)):
        list_suoshuxiaoqu.append(jsonData.RECORDS[i]['所属小区'])

        #把无效字符去掉
        temp4 = jsonData.RECORDS[i]['房屋户型'].replace('\n\t\t\t\t','')
        t4 = str(temp4)
        list_fangwuhuxing.append(t4)
        
        #转换成int型
        temp1 = filter(str.isdigit,jsonData.RECORDS[i]['房屋单价'])
        temp_temp1 = list(temp1)
        del temp_temp1[-1]
        t1 = int("".join(list(temp_temp1)))
        list_fangwudanjia.append(t1)
        
        list_suozaiweizhi.append(jsonData.RECORDS[i]['所在位置'])
        
        #转换成int型
        temp2 =jsonData.RECORDS[i]['建筑面积'].replace('平方米','')
        t2 = float(temp2)
        list_jianzhumianji.append(t2)
        
        #转换成int型
        temp3 = jsonData.RECORDS[i]['参考首付'].replace('万','')
        t3 = float(temp3)
        list_cankaoshoufu.append(t3)
        
        list_jianzaoniandai.append(jsonData.RECORDS[i]['建造年代'])
        list_fangwuchaoxiang.append(jsonData.RECORDS[i]['房屋朝向'])
        list_fangwuleixing.append(jsonData.RECORDS[i]['房屋类型'])
        list_suozailouceng.append(jsonData.RECORDS[i]['所在楼层'])
        list_zhuangxiuchengdu.append(jsonData.RECORDS[i]['装修程度'])
        list_chanquannianxian.append(jsonData.RECORDS[i]['产权年限'])
        list_peitaodianti.append(jsonData.RECORDS[i]['配套电梯'])
        list_fangbennianxian.append(jsonData.RECORDS[i]['房本年限'])
        list_chanquanxingzhi.append(jsonData.RECORDS[i]['产权性质'])
        list_peitaogongnuan.append(jsonData.RECORDS[i]['配套供暖'])
        list_weiyizhufang.append(jsonData.RECORDS[i]['唯一住房'])
        list_yishoufangyuan.append(jsonData.RECORDS[i]['一手房源'])
    
    data = { '所属小区':list_suoshuxiaoqu, 
            '房屋户型':list_fangwuhuxing ,
            '房屋单价':list_fangwudanjia ,
            '所在位置':list_suozaiweizhi ,
            '建筑面积':list_jianzhumianji ,
            '参考首付':list_cankaoshoufu ,
            '建造年代':list_jianzaoniandai,
            '房屋朝向':list_fangwuchaoxiang ,
            '房屋类型':list_fangwuleixing ,
            '所在楼层':list_suozailouceng ,
            '装修程度':list_zhuangxiuchengdu,
            '产权年限':list_chanquannianxian ,
            '配套电梯':list_peitaodianti ,
            '房本年限':list_fangbennianxian ,
            '产权性质':list_chanquanxingzhi ,
            '配套供暖': list_peitaogongnuan ,
            '唯一住房':list_weiyizhufang ,
            '一手房源':list_yishoufangyuan }
    
    frameData = pd.DataFrame(data)
    return frameData

def main():
    #读取各个区的json数据
    #若json文件中有中文,必须加上encoding参数,赋值'utf-8',否则会报错
    df_beijingzhoubian = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\北京周边.json',encoding='utf-8')
    df_changping = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\昌平.json',encoding='utf-8')
    df_chaoyang = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\朝阳.json',encoding='utf-8')
    df_daxing = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\大兴.json',encoding='utf-8')
    df_dongcheng = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\东城.json',encoding='utf-8')
    df_fangshan = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\房山.json',encoding='utf-8')
    df_fengtai = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\丰台.json',encoding='utf-8')
    df_haidian = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\海淀.json',encoding='utf-8')
    df_huairou = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\怀柔.json',encoding='utf-8')
    df_mentougou = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\门头沟.json',encoding='utf-8')
    df_miyun = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\密云.json',encoding='utf-8')
    df_pinggu = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\平谷.json',encoding='utf-8')
    df_shijingshan = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\石景山.json',encoding='utf-8')
    df_shunyi = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\顺义.json',encoding='utf-8')
    df_tongzhou = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\通州.json',encoding='utf-8')
    df_xicheng = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\西城.json',encoding='utf-8')
    df_yanqing = pd.read_json('E:\\PythonDataAnalysis\\webCrawler\\data\\延庆.json',encoding='utf-8')
  
    #导出各区的二手房信息
    beijingzhoubian = json_to_frame(df_beijingzhoubian)
    changping = json_to_frame(df_changping)
    chaoyang = json_to_frame(df_chaoyang)
    daxing = json_to_frame(df_daxing)
    dongcheng = json_to_frame(df_dongcheng)
    fangshan = json_to_frame(df_fangshan)
    fengtai = json_to_frame(df_fengtai)
    haidian = json_to_frame(df_haidian)
    huairou = json_to_frame(df_huairou)
    mentougou = json_to_frame(df_mentougou)
    miyun = json_to_frame(df_miyun)
    pinggu = json_to_frame(df_pinggu)
    shijingshan = json_to_frame(df_shijingshan)
    shunyi = json_to_frame(df_shunyi)
    tongzhou = json_to_frame(df_tongzhou)
    xicheng = json_to_frame(df_xicheng)
    yanqing = json_to_frame(df_yanqing)
    
    #把各个区的信息与其名字整合到一起
    all_district = [beijingzhoubian,changping,chaoyang,daxing,dongcheng,fangshan,fengtai,haidian,huairou,
                    mentougou,miyun,pinggu,shijingshan,shunyi,tongzhou,xicheng,yanqing]
    all_district_name = ['北京周边','昌平','朝阳','大兴','东城','房山','丰台','海淀','怀柔',
                         '门头沟','密云','平谷','石景山','顺义','通州','西城','延庆']
    
    #数据样本信息
    print("———————————————————————————北京各区二手房数量样本———————————————————————————")
    i = 0
    for district in all_district:
        print(all_district_name[i]+": "+str(district.shape[0]))
        i+=1
  
    '''
    数据可视化:直方图
    '''
    plt.figure()
    num = []
    for district in all_district:
        num.append(district.shape[0])
    #画直方图
    plt.bar(all_district_name,num,color='blue')
    #刻度的字体大小
    plt.tick_params(labelsize=6)
    #解决显示中文的问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #设置图标题
    plt.title(u'北京各区二手房数量样本',fontsize=10,color='yellow')
    plt.xlabel(u'北京各城区',color='yellow')
    plt.ylabel(u'二手房数目',color='yellow')
    #显示柱状图中每根柱子的数值
    for a, b in zip(all_district_name, num):
        plt.text(a, b, '%d' %b, ha='center', va='bottom', size=4)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('北京各区二手房数量样本.png')
    plt.show()
    
    
    
        
    print("———————————————————————————北京各区二手房平均单价———————————————————————————")
    i = 0
    pingjun_fangwudanjia = {}
    for district in all_district:
        pingjun_fangwudanjia[all_district_name[i]] = int(district['房屋单价'].mean())
        i+=1
    t = sorted(pingjun_fangwudanjia.items(),key=lambda item:item[1], reverse=True) 
    pingjun_fangwudanjia_sorted = dict(t)
    for i in pingjun_fangwudanjia_sorted:
        print(i+": "+str(pingjun_fangwudanjia_sorted[i])+"元/平方米")
       
    '''
    数据可视化:直方图
    '''
    plt.figure()
    diqu = []
    fangjia = []
    for i in pingjun_fangwudanjia_sorted:
        diqu.append(i)
        fangjia.append(int(pingjun_fangwudanjia_sorted[i]))
    #画直方图
    plt.bar(diqu,fangjia,color='blue')
    #刻度的字体大小
    plt.tick_params(labelsize=6)
    #解决显示中文的问题
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #设置图标题
    plt.title(u'北京各区二手房平均单价',fontsize=10,color='yellow')
    plt.xlabel(u'平均房价',color='yellow')
    plt.ylabel(u'北京各地区',color='yellow')
    #显示柱状图中每根柱子的数值
    for a, b in zip(diqu, fangjia):
        plt.text(a, b, '%.2f' %b, ha='center', va='bottom', size=4)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('北京各区二手房平均单价.png')
    plt.show()
        
        
    print("———————————————————————————北京各区二手房平均参考首付———————————————————————————")
    i = 0
    pingjun_cankaoshoufu = {}
    for district in all_district:
        pingjun_cankaoshoufu[all_district_name[i]] = int(district['参考首付'].mean())
        i+=1
    t = sorted(pingjun_cankaoshoufu.items(),key=lambda item:item[1], reverse=True) 
    pingjun_cankaoshoufu_sorted = dict(t)
    for i in pingjun_cankaoshoufu_sorted:
        print(i+": "+str(pingjun_cankaoshoufu_sorted[i])+"万")
    
    print("———————————————————————————北京各区二手房源平均建筑面积———————————————————————————")
    i = 0
    pingjun_jianzhumianji = {}
    for district in all_district:
        pingjun_jianzhumianji[all_district_name[i]] = int(district['建筑面积'].mean())
        i+=1
    t = sorted(pingjun_jianzhumianji.items(),key=lambda item:item[1], reverse=True) 
    pingjun_jianzhumianji_sorted = dict(t)
    for i in pingjun_jianzhumianji_sorted:
        print(i+": "+str(pingjun_jianzhumianji_sorted[i])+"平方米")
        
    print("———————————————————————北京各区二手房最贵、最便宜的二手房——————————————————————————")
    i = 0
    max_fangwudanjia = {}
    min_fangwudanjua = {}
    for district in all_district:
        max_fangwudanjia[all_district_name[i]] = int(district['房屋单价'].max())
        min_fangwudanjua [all_district_name[i]] = int(district['房屋单价'].min())
        i+=1
    t1 = sorted(max_fangwudanjia.items(),key=lambda item:item[1], reverse=True) 
    t2 = sorted(min_fangwudanjua.items(),key=lambda item:item[1], reverse=True) 
    max_fangwudanjia_sorted = dict(t1)
    min_fangwudanjia_sorted = dict(t2)
    for i in max_fangwudanjia_sorted:
        print(i+": "+str(max_fangwudanjia_sorted[i])+"元/平方米"+"     "+str(min_fangwudanjia_sorted[i])+"元/平方米")   
    
    '''
    数据可视化:直方图
    '''
    plt.figure()
    index = np.arange(0,len(all_district_name))
    maxfangjia = []
    minfangjia = []
    for i in max_fangwudanjia_sorted:
        maxfangjia.append(int(max_fangwudanjia_sorted[i]))
        minfangjia.append(int(min_fangwudanjia_sorted[i]))   
    #画直方图
    bar_width = 0.4
    plt.bar(index,maxfangjia,color='blue',width=bar_width)
    plt.bar(index+bar_width,minfangjia,color='green',width=bar_width)
    #设置x轴的刻度，将构建的xtickslabels代入，同时由于区域比较多，在一块会比较拥挤和重叠，因此设置字体和对齐方式
    xtickslabels=['东城','海淀','西城','朝阳','丰台','昌平','顺义',
                        '通州','大兴','石景山','门头沟','房山','怀柔','密云',
                        '延庆','平谷','北京周边']
    plt.xticks(index,xtickslabels,size='small',rotation=30)
    #刻度的字体大小
    plt.tick_params(labelsize=6)
    #解决显示中文的问题s
    plt.rcParams['font.sans-serif']=['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #设置图标题
    plt.title(u'北京各区二手房最贵、最便宜的二手房',fontsize=10,color='yellow')
    plt.xlabel(u'北京各地区',color='yellow')
    plt.ylabel(u'最贵、最便宜的房价',color='yellow')
    #显示柱状图中每根柱子的数值
    for a, b in zip(index, maxfangjia):
        plt.text(a, b, '%.2f' %b, ha='center', va='bottom', size=4)
        #显示柱状图中每根柱子的数值
    for a, b in zip(index, minfangjia):
        plt.text(a, b, '%.2f' %b, ha='center', va='bottom', size=4)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('北京各区二手房最贵、最便宜的二手房.png')
    plt.show()
     
    print("——————————————————北京市在卖二手房配套电梯、配套供暖——————————————————————————") 
    print(' ')
    print("配套电梯    数量")
    print(haidian['配套电梯'].value_counts()+beijingzhoubian['配套电梯'].value_counts()+
          changping['配套电梯'].value_counts()+chaoyang['配套电梯'].value_counts()+
          daxing['配套电梯'].value_counts()+dongcheng['配套电梯'].value_counts()+
          fangshan['配套电梯'].value_counts()+fengtai['配套电梯'].value_counts()+
          huairou['配套电梯'].value_counts()+mentougou['配套电梯'].value_counts()+
          miyun['配套电梯'].value_counts()+pinggu['配套电梯'].value_counts()+
          shijingshan['配套电梯'].value_counts()+shunyi['配套电梯'].value_counts()+
          tongzhou['配套电梯'].value_counts()+xicheng['配套电梯'].value_counts()+
          yanqing['配套电梯'].value_counts())
    
    print(' ')
    print("配套供暖    数量")
    print(haidian['配套供暖'].value_counts()+beijingzhoubian['配套供暖'].value_counts()+
          changping['配套供暖'].value_counts()+chaoyang['配套供暖'].value_counts()+
          daxing['配套供暖'].value_counts()+dongcheng['配套供暖'].value_counts()+
          fangshan['配套供暖'].value_counts()+fengtai['配套供暖'].value_counts()+
          huairou['配套供暖'].value_counts()+mentougou['配套供暖'].value_counts()+
          miyun['配套供暖'].value_counts()+pinggu['配套供暖'].value_counts()+
          shijingshan['配套供暖'].value_counts()+shunyi['配套供暖'].value_counts()+
          tongzhou['配套供暖'].value_counts()+xicheng['配套供暖'].value_counts()+
          yanqing['配套供暖'].value_counts())
    
    
    print("———————————————————————海淀区二手房信息——————————————————————————")
    print("房屋户型     数量")
    print(haidian['房屋户型'].value_counts())
    
    print(' ')
    print("建造年代     数量")
    print(haidian['建造年代'].value_counts())
    
    print(' ')
    print("房屋朝向    数量")
    print(haidian['房屋朝向'].value_counts())
    
    print(' ')
    print("房屋类型    数量")
    print(haidian['房屋类型'].value_counts())
    
    print(' ')
    print("装修程度    数量")
    print(haidian['装修程度'].value_counts())
    
    print(' ')
    print("产权性质      数量")
    print(haidian['产权性质'].value_counts())
    
    print("—————————————————————北京二手房信息数据分析————————————————————————")
    print("———————————————————————————海淀区各小区平均房价——————————————————————————————")
    data1 = {'所属小区':list(haidian['所属小区']),
            '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian1 = pd.DataFrame(data1)
    grouped1 = dataAnalysis_haidian1['房屋单价'].groupby(dataAnalysis_haidian1['所属小区'])
    print((grouped1.mean().sort_values(ascending = False).round(1)))
    #sort_values()方法可以对值进行排序，默认按照升序，round（1）表示小数点后保留1位小数

    print("————————————————————————海淀区房屋建造年代与平均房价的关系———————————————————————")
    data2 = {'建造年代':list(haidian['建造年代']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian2 = pd.DataFrame(data2)
    grouped2 = dataAnalysis_haidian2['房屋单价'].groupby(dataAnalysis_haidian2['建造年代'])
    print(grouped2.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig1 = plt.figure()
    fig1.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped2.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=4)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房屋建造年代与平均房价的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('建造年代',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list1 = grouped2.mean().sort_values(ascending = False)
    for i in range(len(list1)):
        plt.text(list1[i],i,str(int(list1[i])),color='yellow',fontsize=4)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房屋建造年代与平均房价的关系.png')
    plt.show()

    
    print("——————————————————————————海淀区房屋朝向与平均房价的关系———————————————————————")
    data3 = {'房屋朝向':list(haidian['房屋朝向']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian3 = pd.DataFrame(data3)
    grouped3 = dataAnalysis_haidian3['房屋单价'].groupby(dataAnalysis_haidian3['房屋朝向'])
    print(grouped3.mean().sort_values(ascending = False).round(1))  
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig2 = plt.figure()
    fig2.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped3.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房屋朝向与平均房价的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('房屋朝向',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list2 = grouped3.mean().sort_values(ascending = False)
    for i in range(len(list2)):
        plt.text(list2[i],i,str(int(list2[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房屋朝向与平均房价的关系.png')
    plt.show()
    
    print("——————————————————————————海淀区房屋类型与平均房价的关系———————————————————————")
    data4 = {'房屋类型':list(haidian['房屋类型']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian4 = pd.DataFrame(data4)
    grouped4 = dataAnalysis_haidian4['房屋单价'].groupby(dataAnalysis_haidian4['房屋类型'])
    print(grouped4.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig3 = plt.figure()
    fig3.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped4.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房屋类型与平均房价的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('房屋类型',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list3 = grouped4.mean().sort_values(ascending = False)
    for i in range(len(list3)):
        plt.text(list3[i],i,str(int(list3[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房屋类型与平均房价的关系.png')
    plt.show()
    
    print("——————————————————————————海淀区装修程度与平均房价的关系———————————————————————")
    data5 = {'装修程度':list(haidian['装修程度']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian5 = pd.DataFrame(data5)
    grouped5 = dataAnalysis_haidian5['房屋单价'].groupby(dataAnalysis_haidian5['装修程度'])
    print(grouped5.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig4 = plt.figure()
    fig4.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped5.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区装修程度与平均房价的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('装修程度',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list4 = grouped5.mean().sort_values(ascending = False)
    for i in range(len(list4)):
        plt.text(list4[i],i,str(int(list4[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区装修程度与平均房价的关系.png')
    plt.show()
    
    print("——————————————————————————海淀区房价与是否配套有电梯的关系———————————————————————")
    data6 = {'配套电梯':list(haidian['配套电梯']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian6 = pd.DataFrame(data6)
    grouped6 = dataAnalysis_haidian6['房屋单价'].groupby(dataAnalysis_haidian6['配套电梯'])
    print(grouped6.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig5 = plt.figure()
    fig5.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped6.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房价与是否配套有电梯的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('配套电梯',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list5 = grouped6.mean().sort_values(ascending = False)
    for i in range(len(list5)):
        plt.text(list5[i],i,str(int(list5[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房价与是否配套有电梯的关系.png')
    plt.show()
    
    print("——————————————————————————海淀区房价与产权性质的关系———————————————————————")
    data7 = {'产权性质':list(haidian['产权性质']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian7 = pd.DataFrame(data7)
    grouped7 = dataAnalysis_haidian7['房屋单价'].groupby(dataAnalysis_haidian7['产权性质'])
    print(grouped7.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig6 = plt.figure()
    fig6.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped7.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房价与产权性质的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('产权性质',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list6 = grouped7.mean().sort_values(ascending = False)
    for i in range(len(list6)):
        plt.text(list6[i],i,str(int(list6[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房价与产权性质的关系.png')
    plt.show()
    
    print("——————————————————————————海淀区房价与是否配套有供暖的关系———————————————————————")
    data8 = {'配套供暖':list(haidian['配套供暖']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian8 = pd.DataFrame(data8)
    grouped8 = dataAnalysis_haidian8['房屋单价'].groupby(dataAnalysis_haidian8['配套供暖'])
    print(grouped8.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig7 = plt.figure()
    fig7.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped8.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房价与是否配套有供暖的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('配套供暖',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list7 = grouped8.mean().sort_values(ascending = False)
    for i in range(len(list7)):
        plt.text(list7[i],i,str(int(list7[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房价与是否配套有供暖的关系.png')
    plt.show()
    
    print("——————————————————————————海淀区房价与是否为一手房源的关系———————————————————————")
    data9 = {'一手房源':list(haidian['一手房源']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian9 = pd.DataFrame(data9)
    grouped9 = dataAnalysis_haidian9['房屋单价'].groupby(dataAnalysis_haidian9['一手房源'])
    print(grouped9.mean().sort_values(ascending = False).round(1))
    
    '''
    数据可视化：躺着的柱状图
    '''
    fig8 = plt.figure()
    fig8.add_subplot(1,1,1,facecolor='black',alpha=0.3)
    grouped9.mean().sort_values(ascending = False).round(1).plot(kind='barh',rot=0,fontsize=8)
    #设置标题、x轴、y轴的标签文本
    plt.title('海淀区房价与是否为一手房源的关系',fontsize = 10,color = 'green')
    plt.xlabel('平均房价',fontsize = 8,color = 'green')
    plt.ylabel('一手房源',fontsize = 8,color = 'green')
    #显示柱状图中每根柱子的数值
    list8 = grouped9.mean().sort_values(ascending = False)
    for i in range(len(list8)):
        plt.text(list8[i],i,str(int(list8[i])),color='yellow',fontsize=8)
    #图片像素
    plt.rcParams['savefig.dpi'] = 1500
    #分辨率
    plt.rcParams['figure.dpi'] = 800  
    plt.savefig('海淀区房价与是否为一手房源的关系.png')
    plt.show()
    
    print("———————————————————————海淀区房价与装修程度、房屋类型的关系———————————————————————")
    data10 = {'装修程度':list(haidian['装修程度']),
              '房屋类型':list(haidian['房屋类型']),
             '房屋单价':list(haidian['房屋单价'])}
    dataAnalysis_haidian10 = pd.DataFrame(data10)
    grouped10 = dataAnalysis_haidian10['房屋单价'].groupby([dataAnalysis_haidian10['房屋类型'],dataAnalysis_haidian10['装修程度']])
    print(grouped10.mean().round(1))
 
if __name__ == '__main__':
    main()