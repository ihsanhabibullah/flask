from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Halaman index")
   
@app.route('/about')
def about(): 
    return "<center><h1>ini adalah halaman about<h1><center>"

@app.route('/halo/<name>')
def hali(name) :
    return f"<center><h1>halo {name} !! pue haba<h1><center> "

if __name__ == '__main__' :
    app.run(debug=True)