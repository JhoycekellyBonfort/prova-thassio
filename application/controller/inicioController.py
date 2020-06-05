from application import app
from flask import render_template, current_app
from application.model.entity.video import Video
from application.model.dao.videoDAO import VideoDAO
from application.model.dao.categoriaDAO import CategoriaDAO

@app.route("/")
@app.route("/home")

def inicio():
    lista_de_categorias = current_app.config['categorias'].getCategorias()
    videos_mais_curtidos = current_app.config['videos'].getVideosMaisCurtidos()
    return render_template("inicio.html",lista_de_categorias = lista_de_categorias,videos_mais_curtidos=  videos_mais_curtidos)