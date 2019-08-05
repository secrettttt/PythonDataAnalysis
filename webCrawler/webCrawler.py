# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:36:00 2019

@author: ASUS
"""
import requests,pymysql
from pymysql import cursors
from bs4 import BeautifulSoup
from lxml import etree

class anjuke_second_hand_house():
    def __init__(self):
        self.ALL_District = ['朝阳','海淀','东城','西城','丰台','通州','石景山','昌平','大兴','顺义','房山','门头沟','密云','怀柔','平谷','延庆','北京周边']
        self.District = input(f"{'Please input the district you want to search:'}")
        self.CollectionName = input(f"{'The collectionName of Mysql(or press Enter to use default name.):'}") or str(self.District)
        self.CONNECTION = pymysql.connect(host='localhost',user='root',password='738291159',db='北京二手房信息',charset='utf8',cursorclass=pymysql.cursors.DictCursor)
        self.SQL = f"INSERT INTO {self.CollectionName}(所属小区,房屋户型,房屋单价,所在位置,建筑面积,参考首付,建造年代,房屋朝向,参考月供,房屋类型,所在楼层,装修程度,配套电梯,配套供暖)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"


    def searchByDistrict(self):
        if self.District=='全部':
            for item in self.ALL_District:
                Originpage = 'https://beijing.anjuke.com/sale/'+self.District+'/'
                self.mainfunction(Originpage)
                print(f"All second-hand houses in[{item}]has been saved in database!")
        else:
            Originpage = 'https://beijing.anjuke.com/sale/'+self.District+'/'
            self.mainfunction(Originpage)

    def mainfunction(self,Originpage):
        pagenum = self.total_page_number(str(Originpage+'1'))
        max_pagelength = 90 if pagenum>=90 else pagenum
        for i in range(1,max_pagelength+1):
            pageurl = Originpage +'p'+str(i)+'/#filtersort'
            print(f"Now,it's page【{i}】,the url is:\n",pageurl)
            houselink_list = self.homepage(pageurl)
            for j in range(1,61):
                try:
                    housedata = self.housepage(houselink_list[j-1])
                    self.save_mysql(housedata,j)
                except Exception as e:
                    print(repr(e))
                    pass
                except IndexError:
                    pass

        print("Success!")
            
    def total_page_number(self,url):
#        req = requests.get(url=url)
#        totalnum = etree.HTML(req.text).xpath('/html/body/div[3]/div[3]/div[2]/span[1]/em')[0].text
#        pagenum = int(int(totalnum)/60)
        pagenum = 90
        print(f'totally :【{pagenum}】 pages')
        return pagenum
        
    def homepage(self,homeurl):
        houselink_list = []
        try:
            req = requests.get(homeurl)
            soup = BeautifulSoup(req.text,"lxml")
        except Exception as e:
            print(repr(e))
            self.homepage(homeurl)
        except IndexError:
                    pass
        for item in soup.find_all("div",{"class":"house-title"}):
            if item.a is not None:
                if item.a.attrs['href'] is not None:
                    houselink_list.append(item.a.attrs['href'])
        return houselink_list
        
    def housepage(self,houseurl):
        req = requests.get(houseurl)
        page_obj = BeautifulSoup(req.text,"lxml")
        details = []
        所属小区=房屋户型=房屋单价=所在位置=建筑面积=参考首付=建造年代=房屋朝向=参考月供=房屋类型=所在楼层=装修程度=配套电梯=配套供暖=''
        try:
            obj1 = page_obj.find("ul",{"class":"houseInfo-detail-list clearfix"})

            for item in obj1.find_all("div",{"class":"houseInfo-content"}):
                details.append(item.get_text().strip().strip('\n'))
            所属小区,房屋户型,房屋单价,所在位置,建筑面积,参考首付,建造年代,房屋朝向,参考月供,房屋类型,所在楼层,装修程度,配套电梯,配套供暖=\
            details[0],details[1],details[2],details[3],details[4],details[5],details[6],details[7],details[8],details[9],details[10],details[11],details[12],details[13]
        except Exception as e:
            print(repr(e))
            所属小区=房屋户型=房屋单价=所在位置=建筑面积=参考首付=建造年代=房屋朝向=参考月供=房屋类型=所在楼层=装修程度=配套电梯=配套供暖='NULL'
        except IndexError:
                    pass
        finally:
            housedata = [f'{所属小区}',f'{房屋户型}',f'{房屋单价}',f'{所在位置}',f'{建筑面积}',f'{参考首付}',f'{建造年代}',f'{房屋朝向}',f'{参考月供}',f'{房屋类型}',f'{所在楼层}',f'{装修程度}',f'{配套电梯}',f'{配套供暖}']
            return housedata
        
    def save_mysql(self,house_list,count):
        try:
            with self.CONNECTION.cursor() as cursor:
                cursor.execute(self.SQL,(house_list[0],house_list[1],house_list[2],house_list[3],house_list[4],house_list[5],house_list[6],house_list[7],house_list[8],house_list[9],house_list[10],house_list[11],house_list[12],house_list[13]))
            self.CONNECTION.commit()
            print(house_list)
            print(f"Page【{count}】 has been saved in Mysql!")
        except Exception as e:
            print(repr(e))
        except IndexError:
                    pass
        
spider = anjuke_second_hand_house()
spider.searchByDistrict()