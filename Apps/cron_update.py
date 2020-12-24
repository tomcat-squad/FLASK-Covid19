import mysql.connector,requests,json,datetime

# Link API
url = 'https://api.kawalcorona.com/indonesia/provinsi'

#Data Waktu
time = datetime.datetime.now()

# Membuat Pemintaan Api
response                     = requests.get(url)

#Jawa Barat
jawa_barat_kasus_positif     = response.json()[2]['attributes']['Kasus_Posi']
jawa_barat_kasus_sembuh      = response.json()[2]['attributes']['Kasus_Semb']
jawa_barat_kasus_meninggal   = response.json()[2]['attributes']['Kasus_Meni']

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='tomcat_covid19'
        )
    mycursor = mydb.cursor()

    sql_jawa_barat = "INSERT INTO jawa_barat (id,kasus_positif,kasus_sembuh,kasus_meninggal,tanggal) VALUES (%s,%s,%s,%s,%s)"
    val = [
        (time.strftime("%Y-%m-%d"), jawa_barat_kasus_positif, jawa_barat_kasus_sembuh, jawa_barat_kasus_meninggal,time.strftime("%d %b"))
    ]
    mycursor.executemany(sql_jawa_barat, val)
    mydb.commit()
    print(mycursor.rowcount, "Berhasil Ditambahkan : ",time.strftime("%d %b")) 
except:
    sql_update_jawa_barat = "UPDATE jawa_barat SET kasus_positif = %s, kasus_sembuh = %s, kasus_meninggal = %s, tanggal = %s WHERE id = %s;"
    up_jawa_barat = [
        (jawa_barat_kasus_positif,jawa_barat_kasus_sembuh,jawa_barat_kasus_meninggal,time.strftime("%d %b"),time.strftime("%Y-%m-%d"))
    ]
    mycursor.executemany(sql_update_jawa_barat,up_jawa_barat)
    mydb.commit()
    print("Memperbarui Data : ",time.strftime("%d %b"))