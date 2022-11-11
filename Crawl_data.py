from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import datetime
import pandas as pd
from map import Map
class Crawl_data:
    """"
        Class Crawl_data được xây dựng để crawl data với
        tham số đầu vào là các thư viện cần thiết  đường link dẫn và
        đầu ra là mảng data lưu trữ dữ liệu đã được crawl từ link dẫn

        Class bao gồm các hàm thành phần như set_link, access_link(truy cập link), get_source(lấy open source của page)
        và phần process_data(crawl data và lưu vào mảng kết quả )
    """
    def __init__(self,url=''):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.soup = BeautifulSoup()
        self.url = url
        self.data = pd.DataFrame(
        {'date': [], 'quan': [], 'tinh': [], 'loai_bds': [], 'phap_ly': [], 'duong_truoc_nha': [], 'huong': [],
         'dien_tich': [], 'dai': [], 'rong': [], 'so_phong': [], 'so_lau': [], 'gia': []})
        self.data_ts = pd.DataFrame({'address': [], 'trong_so': []})
        self.dt = datetime.datetime.now()
        self.year = self.dt.year
        self.month = self.dt.month
        self.day = self.dt.day
    def set_url(self,url):
        self.url = url
    def access_link(self):
        self.driver.get(self.url)
    def get_sourcepage(self):
        self.access_link()
        self.soup = BeautifulSoup(self.driver.page_source)
    def get_data(self):
        return self.data
    def get_data_b(self):
        return self.data_ts
    def process_data_1(self,tinh):

        #find link href
        self.get_sourcepage()
        #print(self.soup.prettify())
        link_new = self.soup.find_all('div', {"class": "ct_title"})
        list_new = []
        u = 'https://alonhadat.com.vn/'
        for link in link_new:
            if link.find('a',{"class":"vip"})!= None:
                list_new.append(u+link.find('a',{"class":"vip"}).get("href"))
            else:
                #print(link)
                list_new.append(u+link.find('a').get("href"))

        #crawl data
        for i in list_new:
            self.set_url(i)
            self.get_sourcepage()
            #print(self.soup.prettify())

            data_dic = {'date':'','quan':'','tinh':'','loai_bds':'','phap_ly':'','duong_truoc_nha':'','huong':'','dien_tich':'','dai':'','rong':'','so_phong':'','so_lau':'','gia':''}
            data_b = {'address':'','trong_so':''}
            x = self.soup.find('div',{"class":"address"}).find('span',{"class":"value"}).get_text()
            data_b['address'] = x
            x = x.split(", ")
            data_dic['quan'] = x[len(x)-2]
            data_dic['tinh'] = tinh

            x = self.soup.find('span',{'class':'date'}).get_text()
            x = x[11:len(x)]

            if x == 'Hôm nay':
                    data_dic['date'] = str(self.year) + '-' + str(self.month) + '-' + str(self.day)
            elif x == 'Hôm qua':
                    data_dic['date'] = str(self.year)+'-' + str(self.month) + '-' + str(self.day - 1)
            else:
                    time = x.split('/')
                    data_dic['date'] = time[2] + '-' + time[1] + '-' + time[0]

            x = self.soup.find('div',{"class":"infor"}).find_all('td')
            for id in range(len(x)):
                if (x[id].get_text()=='Loại BDS'):
                    data_dic['loai_bds'] = x[id+1].get_text()
                if (x[id].get_text()=='Pháp lý'):
                    if x[id+1].get_text() == '---':
                        data_dic['phap_ly'] = 'No'
                    else:
                        data_dic['phap_ly'] = 'Yes'
                if (x[id].get_text()=='Số lầu'):
                    data_dic['so_lau'] = x[id+1].get_text()
                if (x[id].get_text()=='Số phòng ngủ'):
                    data_dic['so_phong'] = x[id+1].get_text()
                if (x[id].get_text()=='Chiều dài'):
                    data_dic['dai'] = x[id+1].get_text()
                if (x[id].get_text()=='Chiều ngang'):
                    data_dic['rong'] = x[id+1].get_text()
                if (x[id].get_text() == 'Đường trước nhà'):
                    data_dic['duong_truoc_nha'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Hướng'):
                    data_dic['huong'] = x[id + 1].get_text()


            x = self.soup.find('span',{"class":"price"}).find('span',{"class":"value"})
            data_dic['gia']=x.get_text()

            x = self.soup.find('span', {"class": "square"}).find('span', {"class": "value"})
            data_dic['dien_tich'] = x.get_text()


            #print('1',data_dic)

            self.data = self.data.append(data_dic,ignore_index = True)
            self.data_ts = self.data_ts.append(data_b, ignore_index=True)

    def process_data_2(self,tinh):

        #find link href
        self.get_sourcepage()
        link_new = self.soup.find_all('div', {"class": "ct_title"})
        list_new = []
        u = 'https://123nhadatviet.com/'
        for link in link_new:
            if link.find('a',{"class":"vip"})!= None:
                list_new.append(u+link.find('a',{"class":"vip"}).get("href"))
            else:
                #print(link)
                list_new.append(u+link.find('a').get("href"))

        for i in list_new:
            self.set_url(i)
            self.get_sourcepage()
            # print(self.soup.prettify())
            data_dic = {'date': '', 'quan': '', 'tinh': '', 'loai_bds': '', 'phap_ly': '', 'duong_truoc_nha': '',
                        'huong': '', 'dien_tich': '', 'dai': '', 'rong': '', 'so_phong': '', 'so_lau': '', 'gia': ''}
            data_b = {'address': '', 'trong_so': ''}
            x = self.soup.find('div', {"class": "address"}).find('span', {"class": "value"}).get_text()
            data_b['address'] = x
            x = x.split(", ")
            data_dic['quan'] = x[len(x) - 2]
            data_dic['tinh'] = tinh
            x = self.soup.find('div', {"class": "infor"}).find_all('td')
            for id in range(len(x)):
                if (x[id].get_text() == 'Loại BDS'):
                    data_dic['loai_bds'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Pháp lý'):
                    if x[id + 1].get_text() == '---':
                        data_dic['phap_ly'] = 'No'
                    else:
                        data_dic['phap_ly'] = 'Yes'
                if (x[id].get_text() == 'Số lầu'):
                    data_dic['so_lau'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Số phòng ngủ'):
                    data_dic['so_phong'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Chiều dài'):
                    data_dic['dai'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Chiều ngang'):
                    data_dic['rong'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Hướng'):
                    data_dic['huong'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Giá'):
                    data_dic['gia'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Diện tích'):
                    data_dic['dien_tich'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Lộ giới'):
                    data_dic['duong_truoc_nha'] = x[id + 1].get_text()
                if (x[id].get_text() == 'Ngày đăng'):
                    if x[id + 1].get_text() == 'Hôm nay':
                        data_dic['date'] = str(self.year) + '-' + str(self.month) + '-' + str(self.day)
                    elif x[id + 1].get_text() == 'Hôm qua':
                        data_dic['date'] = str(self.year)+'-' + str(self.month) + '-' + str(self.day - 1)
                    else:
                        time = x[id + 1].get_text().split('/')
                        data_dic['date'] = time[2] + '-' + time[1] + '-' + time[0]

            #print('2',data_dic)
            self.data = self.data.append(data_dic,ignore_index = True)
            self.data_ts = self.data_ts.append(data_b, ignore_index=True)
    def process_data_3(self,tinh):

            # find link href
            self.get_sourcepage()
            # print(self.soup.prettify())
            link_new = self.soup.find_all('p', {"class": "text-large-s m-0 mt-2 name-product"})
            list_new = []
            for link in link_new:
                list_new.append(link.find('a').get("href"))
            # print(list_new)

            for i in list_new:
                self.set_url(i)
                self.get_sourcepage()
                #            print(i)

                data_dic = {'date': '', 'quan': '', 'tinh': '', 'loai_bds': '', 'phap_ly': '', 'duong_truoc_nha': '',
                            'huong': '', 'dien_tich': '', 'dai': '', 'rong': '', 'so_phong': '', 'so_lau': '',
                            'gia': ''}
                data_b = {'address': '', 'trong_so': ''}

                x = self.soup.find('div', {'class': 'display-flex flex-center line-22'}).find('span', {'class': ''})
                text = x.get_text()
                tex = text.split(",")
                if len(tex) ==1:
                    continue
                data_dic['quan'] = tex[len(tex) - 2]

                text = text.lstrip()
                data_b['address'] = text

                x = self.soup.find('div', {'class': 'text-gray text-100 time-since'})['data-time']
                time = (str(x)[0:10]).split('/')
                if len(time) == 1:
                    data_dic['date'] = str(self.year) + '-' + str(self.month) + '-' + str(self.day)
                else:
                    data_dic['date'] = time[2] + '-' + time[1] + '-' + time[0]
                data_dic['tinh'] = tinh

                x = self.soup.find('ul', {"class": "crumb text-medium crumb-text"}).find_all('li')
                s = x[1].find('span').get_text()
                data_dic['loai_bds'] = s

                x = self.soup.find('ul', {"class": "p-0 list-full-info-product"}).find_all('li')
                for i in x:
                    u = i.find_all('span', {"class": ""})
                    if u[0].get_text() == 'Diện tích':
                        data_dic['dien_tich'] = ''.join(u[1].get_text().split())
                    if u[0].get_text() == 'Chiều dài':
                        data_dic['dai'] = ''.join(u[1].get_text().split())
                    if u[0].get_text() == 'Chiều rộng':
                        data_dic['rong'] = ''.join(u[1].get_text().split())
                    if u[0].get_text() == 'Giấy tờ pháp lý':
                        data_dic['phap_ly'] = 'Yes'
                    if u[0].get_text() == 'Phòng ngủ':
                        data_dic['so_phong'] = ''.join(u[1].get_text().split())
                    if u[0].get_text() == 'Số tầng':
                        data_dic['so_lau'] = ''.join(u[1].get_text().split())
                    if u[0].get_text() == 'Hướng':
                        data_dic['huong'] = ''.join(u[1].get_text().split())
                    if u[0].get_text() == 'Đường vào':
                        data_dic['duong_truoc_nha'] = ''.join(u[1].get_text().split())
                if data_dic['phap_ly']  == '' :
                    data_dic['phap_ly'] = 'No'

                x = self.soup.find('span', {'class': 'price'}).get_text()
                data_dic['gia'] = x
                #print('3',data_dic)
                self.data = self.data.append(data_dic,ignore_index = True)
                self.data_ts = self.data_ts.append(data_b, ignore_index=True)

    # def process_data_4(self,tinh):
    #     self.get_sourcepage()
    #     link_new = self.soup.find_all('div',{'class':'reales-title'})
    #
    #     list_new = []
    #     for link in link_new:
    #             list_new.append(link.find('a').get('href'))
    #
    #
    #     for i in list_new:
    #         self.set_url(i)
    #         self.get_sourcepage()
    #
    #         data_dic = {'date': '', 'quan': '', 'tinh': '', 'loai_bds': '', 'phap_ly': '', 'duong_truoc_nha': '',
    #                     'huong': '', 'dien_tich': '', 'dai': '', 'rong': '', 'so_phong': '', 'so_lau': '', 'gia': ''}
    #         data_b = {'address': '', 'trong_so': ''}
    #         data_dic['tinh'] = tinh
    #
    #         x = self.soup.find('div',{'class':'reales-location'}).find('div',{'class':'col-left'}).find('div',{'class':'infor'}).get_text()
    #         x = x.replace(' ','')
    #         x = x.replace('\n',' ')
    #         x = x.split(' ')
    #         data_dic['quan'] = x[2]
    #
    #         x = self.soup.find('div', {'class': 'reales-location'}).find('div', {'class': 'col-right'}).find('div',{'class':'infor'}).get_text()
    #         x = x.split(': ')
    #         time = x[2].split('-')
    #         data_dic['date'] = time[2] + '-' + time[1] + '-' + time[0]
    #
    #         x = self.soup.find('div',{'class':'reals-info-group'}).find('div',{'class':'content'}).find_all('div',{'class':'col-item'})
    #         for i in x:
    #             title = i.find('div',{'class':'infor-note'}).get_text()
    #             if title == 'Giá bán':
    #                 data_dic['gia'] = i.find('div',{'class':'infor-data'}).get_text()
    #             if title == 'Diện tích':
    #                 data_dic['dien_tich'] = i.find('div',{'class':'infor-data'}).get_text()
    #
    #         x = self.soup.find('div',{'class':'reals-house-item opt-mattien'}).find('span',{'class':'value-item'}).get_text()
    #         data_dic['loai_bds'] = x
    #         x = self.soup.find('div', {'class': 'reals-house-item opt-huongnha'}).find('span', {
    #             'class': 'value-item'}).get_text()
    #         data_dic['huong'] = x
    #         x = self.soup.find('div', {'class': 'reals-house-item opt-sotang'}).find('span', {
    #             'class': 'value-item'}).get_text()
    #         data_dic['so_lau'] = x
    #         x = self.soup.find('div', {'class': 'reals-house-item opt-duong'}).find('span', {
    #             'class': 'value-item'}).get_text()
    #         data_dic['duong_truoc_nha'] = x
    #         x = self.soup.find('div', {'class': 'reals-house-item opt-phaply'}).find('span', {
    #             'class': 'value-item'}).get_text()
    #         if x != '':
    #             data_dic['phap_ly'] = 'YES'
    #         else:
    #             data_dic['phap_ly'] = 'NO'
    #         x = self.soup.find('div', {'class': 'address'}).get_text()
    #         data_b['address'] = x



            # data_dic['gia'] = ti['Giá bán:']
            # data_dic['dien_tich'] = ti['Diện tích:']
            # data_dic['phap_ly'] = 'Yes' if "Pháp lý:" in ti else 'No'
            # data_dic['quan'] = ((ti['Vị trí:'].split(","))[len(ti['Vị trí:'].split(",")) - 2])[1:]
            # time = ti['Ngày đăng:'].split('-')
            # data_dic['date'] = time[2] + '-' + time[1] + '-' + time[0]
            #
            # x = self.soup.find('div',{'class':'address'}).get_text()
            # data_b['address'] = x
            #
            # x = self.soup.find('ul',{'class':'list-unstyled property-features-list'}).find_all('li')
            # for j in x:
            #     text = j.get_text().split(':')
            #     if text[0] == 'Chiều ngang':
            #         data_dic['rong'] = text[1][1:]
            #     if text[0] == 'Chiều dài':
            #         data_dic['dai'] = text[1][1:]
            #     if text[0] == 'Loại địa ốc':
            #         data_dic['loai_bds'] = text[1][1:]
            #     if text[0] == 'Đường trước nhà':
            #         data_dic['duong_truoc_nha'] = text[1][1:]
            #     if text[0] == 'Hướng xây dựng':
            #         data_dic['huong'] = text[1][1:]
            #     if text[0] == 'Số lầu':
            #         data_dic['so_lau'] = text[1][1:]
            #     if text[0] == 'Số phòng ngủ':
            #         data_dic['so_phong'] = text[1][1:]
            #
            # print(data_dic)
            # self.data = self.data.append(data_dic, ignore_index=True)
            # self.data_ts = self.data_ts.append(data_b, ignore_index=True)











