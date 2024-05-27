from flask import Blueprint, render_template
from . import db 
bp = Blueprint('alb', __name__, url_prefix='/album/')

@bp.route('/')
def album ():
   consulta = """
             SELECT Title, AlbumId from albums
	         ORDER by Title ASC ;    
	   """
   con = db.get_db()
   res = con.execute(consulta)
   lista_nombre_albumes = res.fetchall()
   pagina = render_template('detalle_album.html', musica=lista_nombre_albumes)
   return pagina

@bp.route('/<int:id>')
def detalle(id):
   con = db.get_db()
   consulta1= """
         SELECT name, a.AlbumId FROM artists ar JOIN albums a ON a.ArtistId = ar.ArtistId
         WHERE ar.ArtistId = ?;  
      """
   consulta2 = """
      SELECT t.name, t.AlbumId as idAl FROM tracks t
      JOIN albums a ON  t.AlbumId = a.AlbumId
      JOIN artists ar ON a.ArtistId = ar.ArtistId
      WHERE t.AlbumId = ?;
        """

   res = con.execute(consulta1, (id,))
   art = res.fetchone()
   res2 = con.execute(consulta2, (id,))
   lista_albumes = res2.fetchall()
   pagina = render_template('detalle_album.html',
                         artis = art ,
                         albumes = lista_albumes )                                                            

   return pagina