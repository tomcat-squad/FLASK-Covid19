from flask import Flask, render_template
from flask_mysql_connector import MySQL
import requests, json, datetime
app = Flask(__name__)

# Mysql Konfiguration
app.config['MYSQL_HOST']        = 'localhost'
app.config['MYSQL_USER']        = 'root'
app.config['MYSQL_PASSWORD']    = ''
app.config['MYSQL_DATABASE']    = 'tomcat_covid19'
mysql = MySQL(app)

# Data Waktu
time = datetime.datetime.now()

# Link API
url = 'https://api.kawalcorona.com/indonesia/provinsi'

# Membuat Pemintaan Api
response          = requests.get(url)
#Jawa Barat
jawa_barat_kasus_positif     = response.json()[1]['attributes']['Kasus_Posi']
jawa_barat_kasus_sembuh      = response.json()[1]['attributes']['Kasus_Semb']
jawa_barat_kasus_meninggal   = response.json()[1]['attributes']['Kasus_Meni']

@app.route('/')
def index():
    conn = mysql.connection

    cur_bekasi_barat = conn.cursor()
    cur_bekasi_barat.execute("SELECT * FROM bekasi_barat;")
    result_bekasi_barat = cur_bekasi_barat.fetchall()

    cur_bekasi_selatan = conn.cursor()
    cur_bekasi_selatan.execute("SELECT * FROM bekasi_selatan;")
    result_bekasi_selatan = cur_bekasi_selatan.fetchall()

    cur_bekasi_timur = conn.cursor()
    cur_bekasi_timur.execute("SELECT * FROM bekasi_timur;")
    result_bekasi_timur = cur_bekasi_timur.fetchall()

    cur_bekasi_utara = conn.cursor()
    cur_bekasi_utara.execute("SELECT * FROM bekasi_utara;")
    result_bekasi_utara = cur_bekasi_utara.fetchall()

    return render_template('data-covid-19.html',
    statistik_bekasi_barat = result_bekasi_barat,
    statistik_bekasi_selatan = result_bekasi_selatan,
    statistik_bekasi_timur = result_bekasi_timur,
    statistik_bekasi_utara = result_bekasi_utara,   
    waktu=time.strftime("%X-%A-%Y"),
    jawa_barat_positif=jawa_barat_kasus_positif, 
    jawa_barat_sembuh=jawa_barat_kasus_sembuh, 
    jawa_barat_meninggal=jawa_barat_kasus_meninggal)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
