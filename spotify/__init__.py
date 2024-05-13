from flask import Flask, render_template

app = Flask(__name__)

with app.app_context():
  from . import db
  db.init_app(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/genero')
def genero ():
  consulta = """
       SELECT Name FROM genres 
       ORDER BY Name;
       """
   
  con = db.get_db()
  res = con.execute(consulta)
  lista_generos = res.fetchall()
  pagina = render_template('genero.html', generos=lista_generos)
  return pagina

@app.route('/musica')
def musica ():
   consulta = """
    SELECT t.Name as cancion, ar.name as artista FROM tracks t 
    JOIN albums a on t.AlbumId = a.AlbumId
    JOIN artists ar on a.ArtistId = ar.ArtistId
    ORDER BY t.Name
	   
	   """
   con = db.get_db()
   res = con.execute(consulta)
   lista_nombre_musica = res.fetchall()
   pagina = render_template('musica.html', musica=lista_nombre_musica)
   return pagina