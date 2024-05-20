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
