from Crawl_data import Crawl_data
import pandas as pd
from map import Map
import cv2 as cv
import os
def Tinh(t):
    if t == 'HCM':
        return 'ho-chi-minh'
    if t == 'Đồng Nai':
        return 'dong-nai'
    if t == 'Bình Dương':
        return 'binh-duong'
    return 'long-an'
def save_csv(data,name):
    data.to_csv(name)
def Map_(path):
    mapp = Map(path)
    mapp.image_capture()
    # mapp.process_txt('result_1.txt')
    # mapp.assign('./Image_address_10000_12000')
    # ts = mapp.get_ts()
    # ts.to_csv('ts_12000_16306.csv')
    #return data

    # for i in range(len(data_ts)):
    #         address = data_ts['address'][i]
    #         image = mapp.image_capture(address)
    #         mapp.detect_object(image)
    #         data_ts['trong_so'][i] = mapp.classification(image)
    # return data_ts
def main():
    # j = 2 # có thể thay đổi trọng số để lấy số lượng data
    # tinh = ['HCM','Đồng Nai','Bình Dương','Long An']
    #
    # #alonhdat_1
    # crawl = Crawl_data()
    # for t in tinh:
    #     print(t)
    #     ww = Tinh(t)
    #     if t == 'HCM':
    #         id = str(2)
    #     if t == 'Long An':
    #         id = str(39)
    #     if t == 'Đồng Nai':
    #         id = str(23)
    #     if t == 'Bình Dương':
    #         id = str(14)
    #     ur = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/'+id+'/' + ww + '/'
    #     # for để duyệt page
    #     for i in range(1,j):
    #          print(i)
    #          if i == 1:
    #              url = 'https://alonhadat.com.vn/nha-dat/can-ban/nha-dat/'+id+'/' + ww + '.html'
    #          else:
    #             url = ur+'trang--'+str(i)+'.html'
    #          crawl.set_url(url)
    #          crawl.process_data_1(t) #process de bat dau crawl
    #
    #
    #
    #     # 123nhadatviet_2
    #
    #     if t == 'HCM':
    #         id = str(2)
    #     if t == 'Long An':
    #         id = str(39)
    #     if t == 'Đồng Nai':
    #         id = str(23)
    #     if t == 'Bình Dương':
    #         id = str(14)
    #     ur = 'https://123nhadatviet.com/rao-vat/can-ban/nha-dat/t'+id+'/' + ww + '/'
    #     for i in range(1, j):
    #          if i == 1:
    #              url = 'https://123nhadatviet.com/rao-vat/can-ban/nha-dat/t'+id+'/' + ww + '.html'
    #          else:
    #              url = ur + 'trang--' + str(i) + '.html'
    #          crawl.set_url(url)
    #          crawl.process_data_2(t)
    #
    #
    #     # nhadatvui_3
    #
    #     if t == 'HCM':
    #         id = str(50)
    #     if t == 'Long An':
    #         id = str(51)
    #     if t == 'Đồng Nai':
    #         id = str(48)
    #     if t == 'Bình Dương':
    #         id = str(47)
    #     ur = 'https://nhadatvui.vn/mua-ban/nha-dat?tinh='+ id +'&page='
    #     for i in range(1,j):
    #         url = ur + str(i)
    #         crawl.set_url(url)
    #         crawl.process_data_3(t)
    #
    #
    # data = crawl.get_data()
    # save_csv(data, 'Data.csv')
    #
    # data = crawl.get_data_b()
    # save_csv(data,'Data_ad.csv')


    ### Khuc nay lay trong so luu vao Data_b
    #data = pd.read_csv('./Data_ad.csv')
    Map_('Ho_chi_minh_24_9.csv')

    #save_csv(data, 'Data_.csv')

if __name__ == '__main__':
    main()
