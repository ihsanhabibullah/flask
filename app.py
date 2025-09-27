from flask import Flask,render_template

app=Flask(__name__)

data={
    "nama":"kumar",
    "tempat_lahir":"Terban",
    "tanggal_lahir":"17-8-1945",
    "jenis_kelamin":"laki-laki",
    "alamat":"Depok",
    "profesi":"Jungler mpl"
}


@app.route('/')
def index():
    return render_template('index.html', title="Home",isi="Selamat Datang Di Web Kagaku No Hikari")

@app.route('/biodata')
def biodata() :
    return render_template('biodata.html',title="Biodata",isi=data)

@app.route('/about')
def about(): 
    return render_template('about.html',title="About",isi="Ini adalah halaman About")

if __name__ == '__main__' :
    app.run(debug=True)