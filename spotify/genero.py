from flask import Blueprint, render_template
from . import db 
bp = Blueprint('genero', __name__, url_prefix='/genero/')


@bp.route('/')
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