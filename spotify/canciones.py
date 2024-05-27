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

