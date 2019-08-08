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


 
if __name__ == '__main__':
    main()