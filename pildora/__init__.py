from flask import Flask
from flask import render_template, request, redirect, url_for

import json

        

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/post')
def post():
    import json
    data = None
    with open('pildoras.json') as json_file: 
        data = json.load(json_file)
    data  = data['posts']
    print('----')
    print(data)
    print(len(data))
    print('----')
    return render_template('post.html',post = data,lon = (int) (len(data)/3) ,indicator = False)

# Funcionalidad vista de un post

@app.route('/view/<title>')
def view(title):
    data = None
    titulo = ''
    cuerpo = ''
    with open('pildoras.json') as json_file:
        data = json.load(json_file)
    data  = data['posts']
    for post in data:
        if post['titulo'] == title:
            titulo = post['titulo']
            cuerpo = post['cuerpo']
            break
     
    return render_template('index.html',titulo = titulo, cuerpo = cuerpo)

# Funcionalidades del administrador

@app.route('/adm/create_post')
def create_post():
    return render_template('publish.html')
    

@app.route('/adm/post')
def post_adm():
    import json
    data = None
    with open('pildoras.json') as json_file: 
        data = json.load(json_file)
    data = data['posts']
    print("real size -> " ,len(data))
    lon = 0
    if (len(data)/3) % 2 != 0:
        lon = (int)(len(data)/3) + 1
    else:
        lon = (int)(len(data)/3)
    print("size -> " , lon )
    return render_template('post.html',post = data, lon = lon, len = len(data),indicator = True)

@app.route('/adm/publish',methods = ['POST', 'GET'])
def publish():
    import json
    titulo = ''
    cuerpo = ''

    if request.method == 'POST':
        titulo = request.form['titulo']
        cuerpo = request.form['cuerpo']
    else:
        titulo = request.args.get('titulo')
        cuerpo = request.args.get('cuerpo')
    if (titulo != '') :
        if (cuerpo != ''):
            data = None
            with open('pildoras.json') as json_file: 
                data = json.load(json_file)
            mydata = {"titulo" : titulo, "cuerpo" : cuerpo}
            data['posts'].append(mydata)
            print(mydata)
            with open('pildoras.json', 'w') as outfile:
                json.dump(data,outfile,indent=4)
    
    return redirect(url_for('post_adm',indicator = True))