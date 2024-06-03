from flask import Blueprint, render_template
from . import db 
bp = Blueprint('cancion', __name__, url_prefix='/canciones/')

@bp.route('/')
def musica ():
   consulta = """
    SELECT t.Name as cancion, ar.name as artista ,ar.artistId as idA FROM tracks t 
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
       SELECT t.Name as cancion, t.Composer as compositor, t.Milliseconds as milisegundos, t.Bytes, g.name as genero FROM tracks t 
       JOIN genres g ON t.GenreId = g.GenreId
       JOIN albums a ON  t.AlbumId = a.AlbumId
       JOIN artists ar ON a.ArtistId = ar.ArtistId
       WHERE TrackId = ?;
   """

   res = con.execute(consulta1, (id,))
   cancion = res.fetchone()
   pagina = render_template('detalle_cancion.html',
                        cancion = cancion)                                                            

   return pagina