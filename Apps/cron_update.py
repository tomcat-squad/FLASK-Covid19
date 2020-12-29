import mysql.connector,requests,json,datetime

# Link API
url = 'https://corona.bekasikota.go.id/public/api/wilayahkecamatan'

# Data Waktu
time = datetime.datetime.now()

# Membuat Pemintaan Api
response                     = requests.get(url)

#Bekasi Barat
bekasi_barat_daily_konfirmasi   = response.json()['data'][4]['kec_daily_konfirmasi_count']

#Bekasi Selatan
bekasi_selatan_daily_konfirmasi = response.json()['data'][5]['kec_daily_konfirmasi_count']

#Bekasi Timur
bekasi_timur_daily_konfirmasi   = response.json()['data'][6]['kec_daily_konfirmasi_count']

#Bekasi Utara
bekasi_utara_daily_konfirmasi   = response.json()['data'][7]['kec_daily_konfirmasi_count']

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='tomcat_covid19'
        )
    mycursor = mydb.cursor()
    
    #DB Insert Bekasi Barat
    sql_bekasi_barat = "INSERT INTO bekasi_barat (id,daily_konfirmasi,tanggal) VALUES (%s,%s,%s);"
    val_bekasi_barat = [
        (time.strftime("%Y-%m-%d"), bekasi_barat_daily_konfirmasi, time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_bekasi_barat, val_bekasi_barat)
    print(mycursor.rowcount, "Bekasi Barat Ditambahkan : ",time.strftime("%d %b"))

    #DB Insert Bekasi Selatan
    sql_bekasi_selatan = "INSERT INTO bekasi_selatan (id,daily_konfirmasi,tanggal) VALUES (%s,%s,%s);"
    val_bekasi_selatan = [
        (time.strftime("%Y-%m-%d"), bekasi_selatan_daily_konfirmasi, time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_bekasi_selatan, val_bekasi_selatan)
    print(mycursor.rowcount, "Bekasi Selatan Ditambahkan : ",time.strftime("%d %b"))

    #DB Insert Bekasi Timur
    sql_bekasi_timur = "INSERT INTO bekasi_timur (id,daily_konfirmasi,tanggal) VALUES (%s,%s,%s);"
    val_bekasi_timur = [
        (time.strftime("%Y-%m-%d"), bekasi_timur_daily_konfirmasi, time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_bekasi_timur, val_bekasi_timur)
    print(mycursor.rowcount, "Bekasi Timur Ditambahkan : ",time.strftime("%d %b"))

    #DB Insert Bekasi Utara
    sql_bekasi_utara = "INSERT INTO bekasi_utara (id,daily_konfirmasi,tanggal) VALUES (%s,%s,%s);"
    val_bekasi_utara = [
        (time.strftime("%Y-%m-%d"), bekasi_utara_daily_konfirmasi, time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_bekasi_utara, val_bekasi_utara)
    print(mycursor.rowcount, "Bekasi Utara Ditambahkan : ",time.strftime("%d %b"))

    mydb.commit()
except:
    #DB Update Bekasi Barat
    sql_bekasi_barat    = "UPDATE bekasi_barat SET daily_konfirmasi = %s, tanggal = %s WHERE id = %s;"
    up_bekasi_barat     = [
        (bekasi_barat_daily_konfirmasi,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_bekasi_barat,up_bekasi_barat)
    print("Memperbarui Data Bekasi Barat : ",time.strftime("%d %b"))

    #DB Update Bekasi Selatan
    sql_bekasi_selatan    = "UPDATE bekasi_selatan SET daily_konfirmasi = %s, tanggal = %s WHERE id = %s;"
    up_bekasi_selatan     = [
        (bekasi_selatan_daily_konfirmasi,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_bekasi_selatan,up_bekasi_selatan)
    print("Memperbarui Data Bekasi Selatan : ",time.strftime("%d %b"))

    #DB Update Bekasi Timur
    sql_bekasi_timur    = "UPDATE bekasi_timur SET daily_konfirmasi = %s, tanggal = %s WHERE id = %s;"
    up_bekasi_timur     = [
        (bekasi_timur_daily_konfirmasi,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_bekasi_timur,up_bekasi_timur)
    print("Memperbarui Data Bekasi Timur : ",time.strftime("%d %b"))

    #DB Update Bekasi Utara
    sql_bekasi_utara    = "UPDATE bekasi_utara SET daily_konfirmasi = %s, tanggal = %s WHERE id = %s;"
    up_bekasi_utara     = [
        (bekasi_utara_daily_konfirmasi,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_bekasi_utara,up_bekasi_utara)
    print("Memperbarui Data Bekasi Utara : ",time.strftime("%d %b"))

    mydb.commit()