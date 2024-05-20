from flask import Blueprint, render_template
from . import db 
bp = Blueprint('artista', __name__, url_prefix='/artistas/')


