from flask import Blueprint, render_template
from . import db 
bp = Blueprint('cancion', __name__, url_prefix='/canciones/')

@bp.route('/')
def musica ():
   consulta = """
    SELECT t.Name as cancion, ar.name as artista,ar.artistId as idA FROM tracks t 
    JOIN albums a on t.AlbumId = a.AlbumId
    JOIN artists ar on a.ArtistId = ar.ArtistId
    ORDER BY t.Name
	   
	   """
   con = db.get_db()
   res = con.execute(consulta)
   lista_nombre_musica = res.fetchall()
   pagina = render_template('musica.html', musica=lista_nombre_musica)
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
   pagina = render_template('detalle_album.html',
                         artistas = artista ,
                         albumes = lista_albumes )                                                            

   return pagina