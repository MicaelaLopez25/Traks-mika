from flask import Blueprint, render_template
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
   pagina = render_template('detalle_album.html', musica=lista_nombre_artistas)
   return pagina

@bp.route('/<int:id>')
def detalle(id):
   con = db.get_db()
   consulta1= """
         SELECT name FROM artists WHERE ArtistId = ?;  
   """
   consulta2 = """
         SELECT a.Title FROM artists n 
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