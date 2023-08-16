from flask import Flask
from flask import request
import pymongo # meng-import library pymongo yang sudah kita install
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://fahreziahmedishlah:123456A@cluster0.1gxia2q.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client['Saxc'] # ganti sesuai dengan nama database kalian
my_collections = db['SAxc'] # ganti sesuai dengan nama collections kalian



def kirim_data(nama,Jurusan,Nilai):
    dataku = {'nama':nama,'Jurusan':Jurusan,'Nilai':Nilai}

    result = my_collections.insert_many([dataku])
    print(result.inserted_ids)



app = Flask(__name__)
@app.route('/',methods=[ 'GET'])
def hello_world():
    return 'GET METHOD'

@app.route('/sensor1',methods=['POST'])
def data():
    nama = request.args.get('nama')
    Jurusan = request.args.get('Jurusan')
    Nilai = request.args.get('Nilai')

    kirim_data(nama=nama, Jurusan=Jurusan, Nilai=Nilai )

    return f'nama: {nama} Jurusan: {Jurusan} Nilai: {Nilai}'


if __name__ == '_main_':
    app.run(host='0.0.0.0')