import mysql.connector
import pandas as pd
db = mysql.connector.connect(user='root', password='kimthoa165', host='127.0.0.1',database='Data_Test')
code_1 = 'CREATE DATABASE `Data_Test`'
code_2 = "CREATE TABLE `Data_Test`.`HCM_House` (`Date` VARCHAR(500) NOT NULL, " \
         "`Quan` VARCHAR(10000) NULL, `Tinh` VARCHAR(5) NULL, `Loai_Bds` VARCHAR(500) NULL," \
         "`Phap_ly` VARCHAR(100) NULL,`Duong_truoc_nha` VARCHAR(500) NULL,`Huong` VARCHAR(500) NULL, " \
         "`Dien_tich` VARCHAR(500) NULL, `Dai` VARCHAR(500) NULL," \
         "`Rong` VARCHAR(100) NULL, `So_phong` VARCHAR(500) NULL, `So_lau` VARCHAR(500) NULL," \
         "`Gia` VARCHAR(500) NULL,`Address` VARCHAR(500) NULL);"

def insert_data(date,quan,tinh,loai_bds,phap_ly,duong_truoc_nha,huong,dien_tich,dai,rong,so_phong,so_lau,gia,address):
    sql = "INSERT INTO HCM_House(Date,Quan,Tinh,Loai_Bds,Phap_ly,Duong_truoc_nha,Huong,Dien_tich,Dai,Rong,So_phong,So_lau,Gia,Address)" \
          "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (date,quan,tinh,loai_bds,phap_ly,duong_truoc_nha,huong,dien_tich,dai,rong,so_phong,so_lau,gia,address)
    cursor = db.cursor()
    cursor.execute(sql,val)
    db.commit()
mycursor = db.cursor()
#mycursor.execute(code_1)
mycursor.execute(code_2)
data = pd.read_csv('/Users/thaotruong/Documents/Job/Ho_chi_minh_24_9.csv')
date = data['date'].tolist()
quan = data['quan'].tolist()
tinh = data['tinh'].tolist()
loai_bds = data['loai_bds'].tolist()
phap_ly = data['phap_ly'].tolist()
duong_truoc_nha = data['duong_truoc_nha'].tolist()
huong = data['huong'].tolist()
dien_tich = data['dien_tich'].tolist()
dai = data['dai'].tolist()
rong = data['rong'].tolist()
so_phong = data['so_phong'].tolist()
so_lau = data['so_lau'].tolist()
gia = data['gia'].tolist()
address = data['address'].tolist()
for i in range(0,len(quan)):
    insert_data(date[i],quan[i],tinh[i],loai_bds[i],
            phap_ly[i],duong_truoc_nha[i],huong[i],
            dien_tich[i],dai[i],rong[i],so_phong[i],
            so_lau[i],gia[i],address[i])

#End
mycursor.close()
db.close()