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
    cur = conn.cursor()
    cur.execute("SELECT * FROM jawa_barat;")
    result_jawa_barat = cur.fetchall()
    return render_template('data-covid-19.html',
    statistik_jawa_barat = result_jawa_barat,    
    waktu=time.strftime("%X-%A-%Y"),
    jawa_barat_positif=jawa_barat_kasus_positif, 
    jawa_barat_sembuh=jawa_barat_kasus_sembuh, 
    jawa_barat_meninggal=jawa_barat_kasus_meninggal)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')