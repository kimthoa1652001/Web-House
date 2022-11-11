from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import cv2 as cv
import pandas as pd
import os
import numpy as np


class Map:
    def __init__(self,path):
        self.map = 'https://www.google.com/maps/@9.6865259,105.5641606,2971m/data=!3m1!1e3?hl=vi-VN'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.dic = {}
        self.path = path
        self.ts = pd.DataFrame({'id': [], 'res': []})
    def get_ts(self):
        return self.ts
    def process_txt(self,path):
        f = open(path, 'r', encoding='utf-8')
        a = f.read()
        a = a.split('data/')
        idd = []
        school = []
        hospital = []
        store = []
        dic = {'id':[],'school':[],'hospital':[],'store':[]}
        for i in range(1,len(a)):
            print(a[i])
            st = a[i].find('/')
            end = a[i].find('.JPG')
            id = a[i][st+1:end]
            idd.append(id)
            if a[i].find('Schools')!=-1:
                school.append(1)
            else:
                school.append(0)
            if a[i].find('Hospitals')!=-1:
                hospital.append(1)
            else:
                hospital.append(0)
            if a[i].find('Stores')!=-1:
                store.append(1)
            else:
                store.append(0)
        dic['id'] = idd
        dic['school'] = school
        dic['hospital'] = hospital
        dic['store'] = store
        self.dic = dic

    def assign(self,dirr):
        # cv.imshow(image)
        for i in os.listdir(dirr):
            dic__ = {'id':'','res':''}
            id = i[:-4]
            print(id)
            dic__['id'] = id
            path = dirr + '/' + i
            image = cv.imread(path)
            gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
            blur = cv.GaussianBlur(gray, (11, 11), 0)
            canny = cv.Canny(blur, 30, 150, 3)
            dilated = cv.dilate(canny, (1, 1), iterations=0)
            (cnt, hierarchy) = cv.findContours(
                dilated.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
            rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            cv.drawContours(rgb, cnt, -1, (0, 255, 0), 2)
            print(len(cnt))
            vt = -1
            res = len(cnt)
            for j in range(len(self.dic['id'])):
                if self.dic['id'][j] == id:
                    vt = j
                    break
            if self.dic['hospital'][vt] == 1:
                res = res+700
            if self.dic['store'][vt] == 1:
                res = res+ 600
            if self.dic['school'][vt] == 1:
                res = res + 500

            if res <= 1000:
                ress = 1
            if 1000 <res<=2500:
                ress = 2
            if 2500<res<=3500:
                ress = 3
            if 3500<res<4500:
                ress = 4
            if res>=4500 :
                ress = 5
            dic__['res'] = ress
            self.ts = self.ts.append(dic__,ignore_index=True)
    def image_capture(self):
        data = pd.read_csv(self.path)
        data['trong_so'] = np.nan
        for id in range(15545,15554):
            print('ok')
            center = data['address'][id]
            self.driver.get(self.map)
            search = self.driver.find_element('id', 'searchboxinput')
            search.send_keys(center)
            search.submit()
            sleep(5)

            find = self.driver.find_element('id', "searchbox-searchbutton")
            find.click()
            sleep(5)

            self.driver.get(self.driver.current_url)
            sleep(5)

            bridge = self.driver.find_elements(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[2]/button')
            bridge[0].click()
            sleep(3)

            dir ='./Image_address/'+str(id)+'.JPG'
            print(dir)
            self.driver.save_screenshot(dir)

            #image = cv.imread(dir)

            #data.loc[id, 'trong_so'] = self.classification(image)

        return data




