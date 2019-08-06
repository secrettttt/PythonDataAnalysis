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
        self.SQL = f"INSERT INTO {self.CollectionName}(所属小区,房屋户型,房屋单价,所在位置,建筑面积,参考首付,建造年代,房屋朝向,参考月供,房屋类型,所在楼层,装修程度,产权年限,配套电梯,房本年限,产权性质,配套供暖,唯一住房,一手房源)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def searchByDistrict(self):
        if self.District=='朝阳':
            Originpage = 'https://beijing.anjuke.com/sale/'+'chaoyang'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='海淀':
            Originpage = 'https://beijing.anjuke.com/sale/'+'haidian'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='东城':
            Originpage = 'https://beijing.anjuke.com/sale/'+'dongcheng'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='西城':
            Originpage = 'https://beijing.anjuke.com/sale/'+'xicheng'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='丰台':
            Originpage = 'https://beijing.anjuke.com/sale/'+'fengtai'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='通州':
            Originpage = 'https://beijing.anjuke.com/sale/'+'tongzhou'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='石景山':
            Originpage = 'https://beijing.anjuke.com/sale/'+'shijingshan'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='昌平':
            Originpage = 'https://beijing.anjuke.com/sale/'+'changping'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='大兴':
            Originpage = 'https://beijing.anjuke.com/sale/'+'daxing'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='顺义':
            Originpage = 'https://beijing.anjuke.com/sale/'+'shunyi'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='房山':
            Originpage = 'https://beijing.anjuke.com/sale/'+'fangshan'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='门头沟':
            Originpage = 'https://beijing.anjuke.com/sale/'+'mentougou'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='密云':
            Originpage = 'https://beijing.anjuke.com/sale/'+'miyun'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='怀柔':
            Originpage = 'https://beijing.anjuke.com/sale/'+'huairou'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='平谷':
            Originpage = 'https://beijing.anjuke.com/sale/'+'pinggu'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='延庆':
            Originpage = 'https://beijing.anjuke.com/sale/'+'yanqing'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")
        elif self.District=='北京周边':
            Originpage = 'https://beijing.anjuke.com/sale/'+'beijingzhoubian'+'/'
            self.mainfunction(Originpage)
            print(f"All second-hand houses in[{self.District}]has been saved in database!")

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
        for item in soup.find_all(class_="house-title"):
            if item.a is not None:
                if item.a.attrs['href'] is not None:
                    houselink_list.append(item.a.attrs['href'])
        return houselink_list
        
    def housepage(self,houseurl):
        req = requests.get(houseurl)
        page_obj = BeautifulSoup(req.text,"lxml")
        details = []
        所属小区=房屋户型=房屋单价=所在位置=建筑面积=参考首付=建造年代=房屋朝向=参考月供=房屋类型=所在楼层=装修程度=产权年限=配套电梯=房本年限=产权性质=配套供暖=唯一住房=一手房源=''
        try:
            obj1 = page_obj.find(class_="houseInfo-wrap")
            for item in obj1.find_all(class_="houseInfo-content"):
                details.append(item.get_text().strip().strip('\n'))
            所属小区,房屋户型,房屋单价,所在位置,建筑面积,参考首付,建造年代,房屋朝向,参考月供,房屋类型,所在楼层,装修程度,产权年限,配套电梯,房本年限,产权性质,配套供暖,唯一住房,一手房源=\
            details[0],details[1],details[2],details[3],details[4],details[5],details[6],details[7],details[8],details[9],details[10],details[11],details[12],details[13],details[14],details[15],details[16],details[17],details[18]
#        except Exception as e:
#            print(repr(e))
        except IndexError:
            pass
        finally:
            housedata = [f'{所属小区}',f'{房屋户型}',f'{房屋单价}',f'{所在位置}',f'{建筑面积}',f'{参考首付}',f'{建造年代}',f'{房屋朝向}',f'{参考月供}',f'{房屋类型}',f'{所在楼层}',f'{装修程度}',f'{产权年限}',f'{配套电梯}',f'{房本年限}',f'{产权性质}',f'{配套供暖}',f'{唯一住房}',f'{一手房源}']
            return housedata
        
    def save_mysql(self,house_list,count):
        try:
            with self.CONNECTION.cursor() as cursor:
                cursor.execute(self.SQL,(house_list[0],house_list[1],house_list[2],house_list[3],house_list[4],house_list[5],house_list[6],house_list[7],house_list[8],house_list[9],house_list[10],house_list[11],house_list[12],house_list[13],house_list[14],house_list[15],house_list[16],house_list[17],house_list[18]))
            self.CONNECTION.commit()
            print(house_list)
            print(f"Page【{count}】 has been saved in Mysql!")
        except Exception as e:
            print(repr(e))
        except IndexError:
            pass
        
spider = anjuke_second_hand_house()
spider.searchByDistrict()