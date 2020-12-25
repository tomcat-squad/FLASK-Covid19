import mysql.connector,requests,json,datetime

# Link API
url = 'https://api.kawalcorona.com/indonesia/provinsi'

#Data Waktu
time = datetime.datetime.now()

# Membuat Pemintaan Api
response                     = requests.get(url)

#DKI Jakarta
dki_jakarta_kasus_positif     = response.json()[0]['attributes']['Kasus_Posi']
dki_jakarta_kasus_sembuh      = response.json()[0]['attributes']['Kasus_Semb']
dki_jakarta_kasus_meninggal   = response.json()[0]['attributes']['Kasus_Meni']

#Jawa Timur
jawa_timur_kasus_positif     = response.json()[1]['attributes']['Kasus_Posi']
jawa_timur_kasus_sembuh      = response.json()[1]['attributes']['Kasus_Semb']
jawa_timur_kasus_meninggal   = response.json()[1]['attributes']['Kasus_Meni']

#Jawa Barat
jawa_barat_kasus_positif     = response.json()[2]['attributes']['Kasus_Posi']
jawa_barat_kasus_sembuh      = response.json()[2]['attributes']['Kasus_Semb']
jawa_barat_kasus_meninggal   = response.json()[2]['attributes']['Kasus_Meni']

#Jawa Tengah
jawa_tengah_kasus_positif     = response.json()[3]['attributes']['Kasus_Posi']
jawa_tengah_kasus_sembuh      = response.json()[3]['attributes']['Kasus_Semb']
jawa_tengah_kasus_meninggal   = response.json()[3]['attributes']['Kasus_Meni']

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='tomcat_covid19'
        )
    mycursor = mydb.cursor()
    
    #DB Insert DKI Jakarta
    sql_dki_jakarta = "INSERT INTO dki_jakarta (id,kasus_positif,kasus_sembuh,kasus_meninggal,tanggal) VALUES (%s,%s,%s,%s,%s)"
    val_dki_jakarta = [
        (time.strftime("%Y-%m-%d"), dki_jakarta_kasus_positif, dki_jakarta_kasus_sembuh, dki_jakarta_kasus_meninggal,time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_dki_jakarta, val_dki_jakarta)
    print(mycursor.rowcount, "DKI Jakarta Ditambahkan : ",time.strftime("%d %b")) 

    #DB Insert Jawa Barat
    sql_jawa_barat = "INSERT INTO jawa_barat (id,kasus_positif,kasus_sembuh,kasus_meninggal,tanggal) VALUES (%s,%s,%s,%s,%s)"
    val_jawa_barat = [
        (time.strftime("%Y-%m-%d"), jawa_barat_kasus_positif, jawa_barat_kasus_sembuh, jawa_barat_kasus_meninggal,time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_jawa_barat, val_jawa_barat)
    print(mycursor.rowcount, "Jawa Barat Ditambahkan : ",time.strftime("%d %b")) 

    #DB Insert Jawa Tengah
    sql_jawa_tengah = "INSERT INTO jawa_tengah (id,kasus_positif,kasus_sembuh,kasus_meninggal,tanggal) VALUES (%s,%s,%s,%s,%s)"
    val_jawa_tengah = [
        (time.strftime("%Y-%m-%d"), jawa_tengah_kasus_positif, jawa_tengah_kasus_sembuh, jawa_tengah_kasus_meninggal,time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_jawa_tengah, val_jawa_tengah)
    print(mycursor.rowcount, "Jawa Tengah Ditambahkan : ",time.strftime("%d %b")) 

    #DB Insert Jawa Timur
    sql_jawa_timur = "INSERT INTO jawa_timur (id,kasus_positif,kasus_sembuh,kasus_meninggal,tanggal) VALUES (%s,%s,%s,%s,%s)"
    val_jawa_timur = [
        (time.strftime("%Y-%m-%d"), jawa_timur_kasus_positif, jawa_timur_kasus_sembuh, jawa_timur_kasus_meninggal,time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_jawa_timur, val_jawa_timur)
    print(mycursor.rowcount, "Jawa Timur Ditambahkan : ",time.strftime("%d %b")) 
    mydb.commit()
except:
    #DB Update DKI Jakarta
    sql_update_dki_jakarta = "UPDATE dki_jakarta SET kasus_positif = %s, kasus_sembuh = %s, kasus_meninggal = %s, tanggal = %s WHERE id = %s;"
    up_dki_jakarta  = [
        (dki_jakarta_kasus_positif,dki_jakarta_kasus_sembuh,dki_jakarta_kasus_meninggal,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_update_dki_jakarta,up_dki_jakarta)
    print("Memperbarui Data DKI Jakarta: ",time.strftime("%d %b"))

    #DB Update Jawa Barat
    sql_update_jawa_barat = "UPDATE jawa_barat SET kasus_positif = %s, kasus_sembuh = %s, kasus_meninggal = %s, tanggal = %s WHERE id = %s;"
    up_jawa_barat = [
        (jawa_barat_kasus_positif,jawa_barat_kasus_sembuh,jawa_barat_kasus_meninggal,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_update_jawa_barat,up_jawa_barat)
    print("Memperbarui Data Jawa Barat: ",time.strftime("%d %b"))

    #DB Update Jawa Tengah
    sql_update_jawa_tengah = "UPDATE jawa_tengah SET kasus_positif = %s, kasus_sembuh = %s, kasus_meninggal = %s, tanggal = %s WHERE id = %s;"
    up_jawa_tengah = [
        (jawa_tengah_kasus_positif,jawa_tengah_kasus_sembuh,jawa_tengah_kasus_meninggal,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_update_jawa_tengah,up_jawa_tengah)
    print("Memperbarui Data Jawa Tengah: ",time.strftime("%d %b"))

    #DB Update Jawa Timur
    sql_update_jawa_timur = "UPDATE jawa_timur SET kasus_positif = %s, kasus_sembuh = %s, kasus_meninggal = %s, tanggal = %s WHERE id = %s;"
    up_jawa_timur = [
        (jawa_timur_kasus_positif,jawa_timur_kasus_sembuh,jawa_timur_kasus_meninggal,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_update_jawa_timur,up_jawa_timur)
    print("Memperbarui Data Jawa Timur: ",time.strftime("%d %b"))
    mydb.commit()