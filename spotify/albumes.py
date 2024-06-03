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
         SELECT title FROM albums
         WHERE albumId = ?;  
      """
   consulta2 = """
      SELECT t.name, t.trackId FROM tracks t
      WHERE t.AlbumId = ?;
        """

   res = con.execute(consulta1, (id,))
   album = res.fetchone()
   res2 = con.execute(consulta2, (id,))
   lista_canciones = res2.fetchall()
   pagina = render_template('detalle_album.html',
                         album = album ,
                         canciones = lista_canciones )                                                            

   return pagina