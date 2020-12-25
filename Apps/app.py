from flask import Flask, render_template
from flask_mysql_connector import MySQL
import requests, json, datetime
app = Flask(__name__)

#Mysql Konfiguration
app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = ''
app.config['MYSQL_DATABASE']    = 'tomcat_covid19'
mysql = MySQL(app)

#Data Waktu
time = datetime.datetime.now()

# Link API
url = 'https://api.kawalcorona.com/indonesia/provinsi'

# Membuat Pemintaan Api
response          = requests.get(url)
#Jawa Barat
jawa_barat_kasus_positif     = response.json()[2]['attributes']['Kasus_Posi']
jawa_barat_kasus_sembuh      = response.json()[2]['attributes']['Kasus_Semb']
jawa_barat_kasus_meninggal   = response.json()[2]['attributes']['Kasus_Meni']

@app.route('/')
def index():
    conn = mysql.connection

    cur_dki_jakarta = conn.cursor()
    cur_dki_jakarta.execute("SELECT * FROM dki_jakarta;")
    result_dki_jakarta = cur_dki_jakarta.fetchall()

    cur_jawa_barat = conn.cursor()
    cur_jawa_barat.execute("SELECT * FROM jawa_barat;")
    result_jawa_barat = cur_jawa_barat.fetchall()

    cur_jawa_tengah = conn.cursor()
    cur_jawa_tengah.execute("SELECT * FROM jawa_tengah;")
    result_jawa_tengah = cur_jawa_tengah.fetchall()

    cur_jawa_timur = conn.cursor()
    cur_jawa_timur.execute("SELECT * FROM jawa_timur;")
    result_jawa_timur = cur_jawa_timur.fetchall()



    return render_template('data-covid-19.html',
    statistik_dki_jakarta = result_dki_jakarta,
    statistik_jawa_barat = result_jawa_barat,
    statistik_jawa_tengah = result_jawa_tengah,
    statistik_jawa_timur = result_jawa_timur,    
    waktu=time.strftime("%X-%A-%Y"),
    jawa_barat_positif=jawa_barat_kasus_positif, 
    jawa_barat_sembuh=jawa_barat_kasus_sembuh, 
    jawa_barat_meninggal=jawa_barat_kasus_meninggal)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')