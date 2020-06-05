from application import app
from flask import render_template, current_app
from application.model.dao.categoriaDAO import CategoriaDAO
@app.route("/categoria/<int:id>")
def categoria(id):
    categoria = current_app.config['categorias'].getCategoriaPorId(id)
    lista_de_categorias = current_app.config['categorias'].getCategorias()
    videos   = categoria.getVideosPorCategoriaId()
    return render_template("categoria.html", categoria = categoria, videos = videos, lista_de_categorias = lista_de_categorias)
