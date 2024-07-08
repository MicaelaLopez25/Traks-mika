from flask import Blueprint, render_template, request, redirect, url_for
from . import db 
bp = Blueprint('artista', __name__, url_prefix='/artistas/')

@bp.route('/')
def artistas ():
   consulta = """
            SELECT name from artists
            ORDER by name ASC ;    
	   """
   con = db.get_db()
   res = con.execute(consulta)
   lista_nombre_artistas = res.fetchall()
   pagina = render_template('detalle_artista.html', musica=lista_nombre_artistas)
   return pagina

@bp.route('/<int:id>')
def detalle(id):
   con = db.get_db()
   consulta1= """
        SELECT name FROM artists WHERE ArtistId = ?;  
   """
   consulta2 = """
         SELECT a.Title, a.albumId FROM artists n 
        JOIN albums a ON  n.ArtistId = a.ArtistId
       WHERE n.ArtistId = ?;
        """

   res = con.execute(consulta1, (id,))
   artista = res.fetchone()
   res = con.execute(consulta2, (id,))
   lista_albumes = res.fetchall()
   pagina = render_template('detalle_artista.html',
                         artista = artista ,
                        albumes = lista_albumes )                                                            

   return pagina

@bp.route('/new', methods=('GET','POST'))
def nuevo():
    if request.method == 'POST':
      name = request.form['name']

      con = db.get_db()
      consulta = """ INSERT INTO artists(name)
                  VALUES  (?) """
      
      con.execute(consulta, (name))
      con.commit()
      return redirect(url_for('artista.artistas'))
    else:
       pagina = render_template('nuevo_artista.html')
       return pagina