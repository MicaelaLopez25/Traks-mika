from flask import Blueprint, render_template
from . import db 
bp = Blueprint('alb', __name__, url_prefix='/album/')

@bp.route('/')
def album ():
   consulta = """
             SELECT Title from albums
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