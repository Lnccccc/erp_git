import dynamic
import pandas as pd
import re
from bs4 import BeautifulSoup
import xlwt
import threading
from time import ctime
from datetime import date
import sqlite3
import pymysql
import uuid
today = str(date.today())

client_name = input("请输入一对一用户名：")
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args

    def getResult(self):
        return self.res

    def run(self):
        print('Starting',self.name,'at:',ctime())
        self.res = self.func(*self.args)
        print(self.name,'finished at:',ctime())

class Keyword(object):
    def __init__(self):

        #self.url = 'https://www.aliexpress.com/wholesale?initiative_id=SB_20180412174003&site=glo&g=y&SearchText=makeup+brushes&needQuery=n&page=1'
        self.front = 'https://www.aliexpress.com/wholesale?initiative_id=SB_20180412174003&site=glo&g=y&SearchText='
        self.behind = '&needQuery=n&page='

    def get_keyword(self, filename='keyword_list/pop_jewery_200.xls'):
        keyword_list = []
        filename = filename
        dataframe = pd.read_excel(filename)
        for i in dataframe['关键词'].values:
            i = i.encode('utf-8').decode()
            keyword_list.append(i)
        return keyword_list[:100] ##爬取前100个关键词

    def get_urlid(self, word, n,):
        id_list = []
        img_list = []
        price_list =[]
        title_list = []
        print('========== KEYWORD IS:%s ==========' % word)
        url = self.front+word+self.behind+n
        try:
            page = dynamic.dynamic(url)
        except:
            print('*---------- CONNECT FAILED ----------*')
            try:
                page = dynamic.dynamic(url)
                print('********** RECONNECT SUCCES **********')
            except:
                print('*----------CONNECT FAILED----------*')
                page = dynamic.dynamic(url)
                print('********** RECONNECT SUCCES **********')
        soup = BeautifulSoup(page.text,'lxml')
        item = soup.find_all('div',{'class':'item'})

        for i in item:
            ### 获取产品id
            info_more = i.find('div',{'class':'info-more'})
            try:
                urlid = info_more.find('input',{'class':'atc-product-id'})['value']
            except:
                urlid = '#######'
            ### 获取产品图片地址
            try:
                img = i.find('img', {'class': 'picCore'})
                if img.get('src'):
                    img_src = img['src'][2:]
                elif img.get('image-src'):
                    img_src = img['image-src'][2:]
                else:
                    img_src = '####'
            except:
                img_src = '####'
            ### 获取产品标题
            try:
                title = i.find('a',{'class':'history-item product '})['title']
                title = re.sub(r"'",' ',title)
                title = re.sub(r'"',' ',title)

            except:
                title = '####'
            ### 获取产品价格
            try:
                price_span = i.find_all('span',{'class':'price price-m'})
                for i in price_span:
                    price = i.find('span',{'class':'value'}).get_text()
            except:
                price = '####'
            price_list.append(price)
            img_list.append(img_src)
            id_list.append(urlid)
            title_list.append(title)
        return id_list,img_list,price_list,title_list


    def ExcelWrite(self, keyword_list, urlid_list,page_list,rank_list,filename):
        wb = xlwt.Workbook(encoding='utf-8')
        sh = wb.add_sheet("Aliexpress-Saleeeee")
        sh.write(0, 0, 'KEYWORD')
        sh.write(0, 1, 'URLID')
        sh.write(0, 2, 'PAGE')
        sh.write(0, 3, 'RANK')
        for i in range(len(urlid_list)):
            sh.write(i+1,0,keyword_list[i])
            sh.write(i+1,1,urlid_list[i])
            sh.write(i+1,2,page_list[i])
            sh.write(i+1,3,rank_list[i])
        wb.save(filename+'.xls')

    def DatabaseWirte(self,urlid_list,keyword_list,page_list,rank_list,img_list,title_list,price_list):
        conn = pymysql.connect(host='gz-cdb-3p82wwqf.sql.tencentcdb.com',port=62982,user='root',passwd='pjq_XXX_1022',db='keyword')
        print("连接数据库成功")

        cursor = conn.cursor()
        try:
            cursor.execute("CREATE TABLE inquire_keyword3 (picSrc TEXT,Urlid VARCHAR(20),Keyword VARCHAR(50),Page VARCHAR(5), Rank VARCHAR(5),Client VARCHAR(20), updataTime DATETIME)")
        except:
            print('表已存在')
        print("正在写入数据库...")

        for i in range(len(urlid_list)):
            #sql = """INSERT INTO keyword VALUES ('%s','%s',%s,%s)""" % keyword_list[i],urlid_list[i],page_list[i],rank_list[i]
            word = re.sub(r'\+',' ',keyword_list[i])
            cursor.execute("INSERT INTO inquire_keyword3 (picsrc,urlid,keyword,page,rank,client,title,price,updatatime) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s',now())" % (str(img_list[i]),str(urlid_list[i]),str(word),str(page_list[i]),str(rank_list[i]),str(client_name),str(title_list[i]),str(price_list[i])))
        cursor.close()
        conn.commit()
        conn.close()

keyword = Keyword()
word_list = keyword.get_keyword()
_urlid = []
_word = []
_count = []
_rank = []
_img = []
_price = []
_title = []
lock = threading.Lock()
def master():
    n = 0
    while word_list:
        count = 0
        word = word_list.pop()
        print('还剩%d个关键词...' %len(word_list))
        word = re.sub(r' ','+',word)
        while count<5:
            try:
                urlid_list,img_list,price_list,title_list = keyword.get_urlid(word,str(count+1))
                for i in urlid_list:
                    lock.acquire()
                    try:
                        rank = int(urlid_list.index(i))+1
                        _rank.append(rank)
                        _word.append(word)
                        _urlid.append(i)
                        _count.append(str(count+1))
                        _img.append(img_list[urlid_list.index(i)])
                        _price.append(price_list[urlid_list.index(i)])
                        _title.append(title_list[urlid_list.index(i)])

                    finally:
                        lock.release()

                count += 1
            except Exception as e:

                print(e)
                print('*---------- CODE WRONG ----------*')
                break
        n +=1

t1 = MyThread(master,(),'t1')
t2 = MyThread(master,(),'t2')
t3 = MyThread(master,(),'t3')
t4 = MyThread(master,(),'t4')
t5 = MyThread(master,(),'t5')
t6 = MyThread(master,(),'t6')
t7 = MyThread(master,(),'t7')
t8 = MyThread(master,(),'t8')
# t9 = MyThread(master,(),'t9')
# t10 = MyThread(master,(),'t10')
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
# t9.start()
# t10.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
# t9.join()
# t10.join()
keyword.DatabaseWirte(_urlid,_word,_count,_rank,_img,_title,_price)
#conn = sqlite3.connect('keyword_database.db')
#cursor = conn.cursor()
#cursor.execute("SELECT * FROM keyword")
#for each in cursor.fetchall():
    #print(each)

# QUESION:
# 数据输出问题
# 爬取失败问题，如何保证数据一定会获取成功？
